const form = document.getElementById("resumeForm");

form.addEventListener("submit", async function(event) {
    event.preventDefault();

    const resumeFile = document.getElementById("resumeFile").files[0];
    const jobDescription = document.getElementById("jobDescription").value;
    const loading = document.getElementById("loading");

    const formData = new FormData();
    formData.append("resume", resumeFile);
    formData.append("job_description", jobDescription);
//    console.log("FormData: created");

loading.hidden = false;

try{
    const response = await fetch("http://127.0.0.1:8000/analyze", {
    method: "POST",
    body: formData
});

const data = await response.json();
const results = document.getElementById("results");

results.innerHTML = `
  <h2>Analysis Result</h2>
  <p><strong>Overall Score:</strong> ${data.overall_score}/100</p>
  <p><strong>ATS Score:</strong> ${data.ats_score}/100</p>
  <h3>Job Match Summary</h3>
  <p>${data.job_match_summary}</p>
  ${renderList("Strengths", data.strengths)}
  ${renderList("Weaknesses", data.weaknesses)}
  ${renderList("Missing Skills", data.missing_skills)}
  ${renderList("Missing Technologies", data.missing_technologies)}
  ${renderList("Improvements", data.improvements)}
  ${renderList("Project Suggestions", data.project_suggestions)}
`;

}
finally{    loading.hidden = true;
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