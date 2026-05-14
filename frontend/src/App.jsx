import { useState } from "react";
import API from "./services/api";

function App() {
  const [formData, setFormData] = useState({
    hardness: "",
    density: "",
    temperature: "",
    load: "",
    speed: "",
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    setLoading(true);

    try {
      const response = await API.post("/recommend", {
        hardness: Number(formData.hardness),
        density: Number(formData.density),
        temperature: Number(formData.temperature),
        load: Number(formData.load),
        speed: Number(formData.speed),
      });

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Backend Error");
    } finally {
      setLoading(false);
    }
  };

  const inputStyle = {
    padding: "14px",
    borderRadius: "12px",
    border: "1px solid #334155",
    backgroundColor: "#1e293b",
    color: "white",
    fontSize: "16px",
    outline: "none",
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        background:
          "linear-gradient(to bottom right, #0f172a, #111827, #1e293b)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        padding: "40px",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <div
        style={{
          width: "100%",
          maxWidth: "1100px",
          background: "rgba(255,255,255,0.05)",
          backdropFilter: "blur(10px)",
          border: "1px solid rgba(255,255,255,0.1)",
          borderRadius: "24px",
          padding: "40px",
          boxShadow: "0px 10px 40px rgba(0,0,0,0.4)",
        }}
      >
        <div style={{ marginBottom: "40px" }}>
          <h1
            style={{
              fontSize: "42px",
              color: "#f8fafc",
              marginBottom: "10px",
            }}
          >
            AI Material Recommendation System
          </h1>

          <p
            style={{
              color: "#cbd5e1",
              fontSize: "18px",
            }}
          >
            Predict tribological properties and discover the best material recommendations using machine learning.
          </p>
        </div>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "1fr 1fr",
            gap: "40px",
          }}
        >
          {/* LEFT SIDE FORM */}

          <div
            style={{
              background: "#111827",
              padding: "30px",
              borderRadius: "20px",
              border: "1px solid #1e293b",
            }}
          >
            <h2
              style={{
                color: "#f8fafc",
                marginBottom: "25px",
                fontSize: "28px",
              }}
            >
              Input Parameters
            </h2>

            <form
              onSubmit={handleSubmit}
              style={{
                display: "grid",
                gap: "18px",
              }}
            >
              <input
                type="number"
                name="hardness"
                placeholder="Hardness"
                onChange={handleChange}
                required
                style={inputStyle}
              />

              <input
                type="number"
                name="density"
                placeholder="Density"
                onChange={handleChange}
                required
                style={inputStyle}
              />

              <input
                type="number"
                name="temperature"
                placeholder="Temperature"
                onChange={handleChange}
                required
                style={inputStyle}
              />

              <input
                type="number"
                name="load"
                placeholder="Load"
                onChange={handleChange}
                required
                style={inputStyle}
              />

              <input
                type="number"
                name="speed"
                placeholder="Speed"
                onChange={handleChange}
                required
                style={inputStyle}
              />

              <button
                type="submit"
                style={{
                  marginTop: "10px",
                  padding: "15px",
                  background:
                    "linear-gradient(to right, #2563eb, #7c3aed)",
                  border: "none",
                  borderRadius: "14px",
                  color: "white",
                  fontSize: "17px",
                  fontWeight: "bold",
                  cursor: "pointer",
                  transition: "0.3s",
                }}
              >
                {loading ? "Predicting..." : "Recommend Material"}
              </button>
            </form>
          </div>

          {/* RIGHT SIDE RESULTS */}

          <div
            style={{
              background: "#111827",
              padding: "30px",
              borderRadius: "20px",
              border: "1px solid #1e293b",
              overflowY: "auto",
              maxHeight: "700px",
            }}
          >
            <h2
              style={{
                color: "#f8fafc",
                marginBottom: "25px",
                fontSize: "28px",
              }}
            >
              Prediction Results
            </h2>

            {!result && (
              <div
                style={{
                  color: "#94a3b8",
                  marginTop: "80px",
                  textAlign: "center",
                  fontSize: "18px",
                }}
              >
                Results will appear here after prediction.
              </div>
            )}

            {result && (
              <div>
                {/* PREDICTED VALUES */}

                <div
                  style={{
                    background: "#1e293b",
                    padding: "20px",
                    borderRadius: "16px",
                    marginBottom: "25px",
                  }}
                >
                  <h3
                    style={{
                      color: "#38bdf8",
                      marginBottom: "15px",
                    }}
                  >
                    Predicted Properties
                  </h3>

                  <p style={{ color: "#f8fafc", fontSize: "17px" }}>
                    <strong>Wear Rate:</strong>{" "}
                    {result.predicted_properties.WearRate}
                  </p>

                  <p style={{ color: "#f8fafc", fontSize: "17px" }}>
                    <strong>Friction Coefficient:</strong>{" "}
                    {
                      result.predicted_properties
                        .FrictionCoefficient
                    }
                  </p>
                </div>

                {/* MATERIAL RECOMMENDATIONS */}

                <h3
                  style={{
                    color: "#38bdf8",
                    marginBottom: "15px",
                  }}
                >
                  Recommended Materials
                </h3>

                {result.recommended_materials.map(
                  (material, index) => (
                    <div
                      key={index}
                      style={{
                        background: "#1e293b",
                        padding: "20px",
                        borderRadius: "16px",
                        marginBottom: "18px",
                        borderLeft: "5px solid #7c3aed",
                      }}
                    >
                      <h3
                        style={{
                          color: "#f8fafc",
                          marginBottom: "12px",
                          fontSize: "24px",
                        }}
                      >
                        {material.Material}
                      </h3>

                      <div
                        style={{
                          display: "grid",
                          gap: "8px",
                          color: "#cbd5e1",
                          fontSize: "16px",
                        }}
                      >
                        <p>
                          <strong>Similarity Score:</strong>{" "}
                          {material.SimilarityScore}%
                        </p>

                        <p>
                          <strong>Wear Rate:</strong>{" "}
                          {material.WearRate}
                        </p>

                        <p>
                          <strong>Friction Coefficient:</strong>{" "}
                          {
                            material.FrictionCoefficient
                          }
                        </p>
                      </div>
                    </div>
                  )
                )}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;


