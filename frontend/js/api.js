// Simple frontend helper to call backend APIs from Vercel-hosted static pages.
// Set this to your deployed backend base URL (Render/Railway).
// Example: const API_BASE_URL = "https://your-backend.onrender.com";
const API_BASE_URL = "http://127.0.0.1:8000"; // change for production

const JobApi = {
    async fetchJobs(params = {}) {
        if (!API_BASE_URL) return [];
        const url = new URL(API_BASE_URL + "/api/jobs/");
        if (params.search) url.searchParams.set("search", params.search);
        if (params.location) url.searchParams.set("location", params.location);
        const res = await fetch(url);
        if (!res.ok) throw new Error("Failed to fetch jobs");
        return await res.json();
    },

    async fetchLatestJobs() {
        if (!API_BASE_URL) return [];
        const res = await fetch(API_BASE_URL + "/api/jobs/?limit=5");
        if (!res.ok) throw new Error("Failed to fetch jobs");
        return await res.json();
    },

    async fetchRecommendedJobs() {
        if (!API_BASE_URL) return [];
        const res = await fetch(API_BASE_URL + "/api/recommended-jobs/");
        if (!res.ok) throw new Error("Failed to fetch recommended jobs");
        return await res.json();
    },
};

window.JobApi = JobApi;

