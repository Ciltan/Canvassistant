import { useState, useEffect, useRef } from "react";

const API_BASE = "http://localhost:8000";

// ── API helpers ─────────────────────────────────────────
async function apiFetch(endpoint, body) {
  const res = await fetch(`${API_BASE}${endpoint}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || `Request failed (${res.status})`);
  }
  return res.json();
}

async function fetchCourses() {
  const res = await fetch(`${API_BASE}/courses`);
  if (!res.ok) throw new Error("Failed to fetch courses");
  const data = await res.json();
  return data.courses || [];
}

// ── Tab Components ──────────────────────────────────────

function ChatTab() {
  const [messages, setMessages] = useState(() => {
    const saved = localStorage.getItem("chat_messages");
    return saved ? JSON.parse(saved) : [];
  });
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [courses, setCourses] = useState([]);
  const [selectedCourse, setSelectedCourse] = useState(() => {
    return localStorage.getItem("chat_selected_course") || "";
  });
  const messagesEndRef = useRef(null);

  useEffect(() => {
    localStorage.setItem("chat_messages", JSON.stringify(messages));
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  useEffect(() => {
    localStorage.setItem("chat_selected_course", selectedCourse);
  }, [selectedCourse]);

  useEffect(() => {
    fetchCourses().then(setCourses).catch(() => {});
  }, []);

  const sendMessage = async () => {
    const question = input.trim();
    if (!question || loading) return;

    setInput("");
    setMessages((prev) => [...prev, { role: "user", content: question }]);
    setLoading(true);

    try {
      const data = await apiFetch("/query", { 
        question,
        course_name: selectedCourse || null
      });
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: data.answer,
          sources: data.sources,
        },
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: `Error: ${err.message}` },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const clearChat = () => {
    if (window.confirm("Clear all chat messages?")) {
      setMessages([]);
      localStorage.removeItem("chat_messages");
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <>
      <div className="chat-header-actions">
        <select 
          className="chat-course-select"
          value={selectedCourse} 
          onChange={(e) => setSelectedCourse(e.target.value)}
        >
          <option value="">Search all materials</option>
          {courses.map((c) => (
            <option key={c} value={c}>Focus on: {c}</option>
          ))}
        </select>
        <button className="clear-chat-btn" onClick={clearChat} title="Clear history">
          🗑️
        </button>
      </div>

      <div className="content">
        <div className="chat-messages">
          {messages.length === 0 && (
            <div className="welcome-message">
              <div className="welcome-icon">🎓</div>
              <h2>Canvas Study AI</h2>
              <p>
                Ask any question about your course materials.
                <br />
                {selectedCourse ? `Currently focusing on: ${selectedCourse}` : "Searching across all indexed modules."}
              </p>
            </div>
          )}
          {messages.map((msg, i) => (
            <div key={i} className={`message ${msg.role}`}>
              <div>{msg.content}</div>
              {msg.sources && msg.sources.length > 0 && (
                <div className="sources">
                  📎 Sources:{" "}
                  {msg.sources.map((s, j) => (
                    <span key={j}>
                      {s.file} (p.{s.page})
                    </span>
                  ))}
                </div>
              )}
            </div>
          ))}
          {loading && (
            <div className="message assistant">
              <div className="loading" style={{ padding: "8px 0" }}>
                <div className="spinner" />
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>
      </div>
      <div className="chat-input-area">
        <input
          type="text"
          placeholder={selectedCourse ? `Ask about ${selectedCourse}...` : "Ask about your courses..."}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          disabled={loading}
        />
        <button className="send-btn" onClick={sendMessage} disabled={loading || !input.trim()}>
          Send
        </button>
      </div>
    </>
  );
}

function TopicsTab() {
  const [courses, setCourses] = useState([]);
  const [selectedCourse, setSelectedCourse] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchCourses().then(setCourses).catch(() => {});
  }, []);

  const analyze = async () => {
    setLoading(true);
    setError("");
    setResult(null);
    try {
      const data = await apiFetch("/topics", {
        course_name: selectedCourse || null,
      });
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="content">
      <div className="course-selector">
        <label>Select Course (optional)</label>
        <select value={selectedCourse} onChange={(e) => setSelectedCourse(e.target.value)}>
          <option value="">All Courses</option>
          {courses.map((c) => (
            <option key={c} value={c}>{c}</option>
          ))}
        </select>
      </div>
      <button className="action-btn" onClick={analyze} disabled={loading}>
        {loading ? "Analyzing..." : "🎯 Identify Exam Topics"}
      </button>
      {error && <div className="error-msg">⚠️ {error}</div>}
      {loading && (
        <div className="loading">
          <div className="spinner" />
          Analyzing course materials...
        </div>
      )}
      {result && (
        <div className="result-card">
          <h3>Likely Exam Topics</h3>
          <div className="result-content">{result.topics}</div>
          <div className="result-meta">
            Courses: {result.courses_analyzed?.join(", ")} · {result.chunks_analyzed} chunks analyzed
          </div>
        </div>
      )}
    </div>
  );
}

function PracticeTab() {
  const [courses, setCourses] = useState([]);
  const [selectedCourse, setSelectedCourse] = useState("");
  const [topic, setTopic] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchCourses().then(setCourses).catch(() => {});
  }, []);

  const generate = async () => {
    setLoading(true);
    setError("");
    setResult(null);
    try {
      const data = await apiFetch("/practice", {
        course_name: selectedCourse || null,
        topic: topic || null,
      });
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="content">
      <div className="course-selector">
        <label>Select Course (optional)</label>
        <select value={selectedCourse} onChange={(e) => setSelectedCourse(e.target.value)}>
          <option value="">All Courses</option>
          {courses.map((c) => (
            <option key={c} value={c}>{c}</option>
          ))}
        </select>
      </div>
      <div className="topic-input">
        <label>Focus Topic (optional)</label>
        <input
          type="text"
          placeholder="e.g. Binary search trees, Integration..."
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
        />
      </div>
      <button className="action-btn" onClick={generate} disabled={loading}>
        {loading ? "Generating..." : "📝 Generate Practice Questions"}
      </button>
      {error && <div className="error-msg">⚠️ {error}</div>}
      {loading && (
        <div className="loading">
          <div className="spinner" />
          Generating practice questions...
        </div>
      )}
      {result && (
        <div className="result-card">
          <h3>Practice Questions</h3>
          <div className="result-content">{result.questions}</div>
        </div>
      )}
    </div>
  );
}

function SummaryTab() {
  const [courses, setCourses] = useState([]);
  const [selectedCourse, setSelectedCourse] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchCourses().then(setCourses).catch(() => {});
  }, []);

  const summarize = async () => {
    if (!selectedCourse) {
      setError("Please select a course to summarize.");
      return;
    }
    setLoading(true);
    setError("");
    setResult(null);
    try {
      const data = await apiFetch("/summarize", {
        course_name: selectedCourse,
      });
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="content">
      <div className="course-selector">
        <label>Select Course</label>
        <select value={selectedCourse} onChange={(e) => setSelectedCourse(e.target.value)}>
          <option value="">— Choose a course —</option>
          {courses.map((c) => (
            <option key={c} value={c}>{c}</option>
          ))}
        </select>
      </div>
      <button className="action-btn" onClick={summarize} disabled={loading || !selectedCourse}>
        {loading ? "Summarizing..." : "📚 Summarize Course"}
      </button>
      {error && <div className="error-msg">⚠️ {error}</div>}
      {loading && (
        <div className="loading">
          <div className="spinner" />
          Summarizing lecture slides...
        </div>
      )}
      {result && (
        <div className="result-card">
          <h3>Course Summary — {result.course}</h3>
          <div className="result-content">{result.summary}</div>
          <div className="result-meta">
            {result.chunks_analyzed} chunks analyzed
          </div>
        </div>
      )}
    </div>
  );
}

// ── Main App ──────────────────────────────────────────────
const TABS = [
  { key: "chat", icon: "💬", label: "Chat" },
  { key: "topics", icon: "🎯", label: "Topics" },
  { key: "practice", icon: "📝", label: "Practice" },
  { key: "summary", icon: "📚", label: "Summary" },
];

export default function App() {
  const [activeTab, setActiveTab] = useState(() => {
    return localStorage.getItem("active_tab") || "chat";
  });
  const [online, setOnline] = useState(false);

  useEffect(() => {
    localStorage.setItem("active_tab", activeTab);
  }, [activeTab]);

  // Check if backend is reachable
  useEffect(() => {
    const check = async () => {
      try {
        const res = await fetch(`${API_BASE}/`);
        setOnline(res.ok);
      } catch {
        setOnline(false);
      }
    };
    check();
    const interval = setInterval(check, 15000);
    return () => clearInterval(interval);
  }, []);

  return (
    <>
      {/* Header */}
      <div className="header">
        <span className="header-icon">🎓</span>
        <h1>Canvas Study AI</h1>
        <div className={`status-dot ${online ? "" : "offline"}`} title={online ? "Backend connected" : "Backend offline"} />
      </div>

      {/* Tab Bar */}
      <div className="tab-bar">
        {TABS.map((tab) => (
          <button
            key={tab.key}
            className={`tab-btn ${activeTab === tab.key ? "active" : ""}`}
            onClick={() => setActiveTab(tab.key)}
          >
            <span className="tab-icon">{tab.icon}</span>
            {tab.label}
          </button>
        ))}
      </div>

      {/* Tab Content */}
      {activeTab === "chat" && <ChatTab />}
      {activeTab === "topics" && <TopicsTab />}
      {activeTab === "practice" && <PracticeTab />}
      {activeTab === "summary" && <SummaryTab />}
    </>
  );
}
