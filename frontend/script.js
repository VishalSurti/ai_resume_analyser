const form = document.getElementById("resumeForm");

form.addEventListener("submit", async function(event) {
    event.preventDefault();

    const resumeFile = document.getElementById("resumeFile").files[0];
    const jobDescription = document.getElementById("jobDescription").value;
    const loading = document.getElementById("loading");
    const analyzeButton = document.getElementById("analyzeButton");
    const results = document.getElementById("results");

    const formData = new FormData();
    formData.append("resume", resumeFile);
    formData.append("job_description", jobDescription);
//    console.log("FormData: created");

loading.hidden = false;

try{

    analyzeButton.disabled = true;
    analyzeButton.textContent = "Analyzing...";
    results.innerHTML = "";
    results.hidden = true;
    results.innerHTML = "";

    const response = await fetch("http://127.0.0.1:8000/analyze", {
    method: "POST",
    body: formData
});

const data = await response.json();

if (!response.ok) {
        throw new Error(data.detail || "Analysis failed. Please try again.");
    }

results.innerHTML = `
  <h2>Analysis Result</h2>
  <div class="score-container">
    <div class="score-card">
        <h3>Overall Score</h3>
        <p>${data.overall_score}/100</p>
    </div>

    <div class="score-card">
        <h3>ATS Score</h3>
        <p>${data.ats_score}/100</p>
    </div>
</div>
  <h3>Job Match Summary</h3>
  <p>${data.job_match_summary}</p>
  ${renderList("Strengths", data.strengths)}
  ${renderList("Weaknesses", data.weaknesses)}
  ${renderList("Missing Skills", data.missing_skills)}
  ${renderList("Missing Technologies", data.missing_technologies)}
  ${renderList("Improvements", data.improvements)}
  ${renderList("Project Suggestions", data.project_suggestions)}
`;

results.hidden = false;

}
catch (error) {
    results.innerHTML = `
        <p class="error">${error.message}</p>
    `;
    results.hidden = false;
} 
finally{    
    loading.hidden = true;
    analyzeButton.disabled = false;
    analyzeButton.textContent = "Analyze Resume";
}

});

function renderList(title, items) {
    if (!items || items.length === 0) {
        return "";
    }

    return `
        <h3>${title}</h3>
        <ul>
            ${items.map(item => `<li>${item}</li>`).join("")}
        </ul>
    `;
}