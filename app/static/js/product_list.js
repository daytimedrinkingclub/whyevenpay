let offset = 10;
const limit = 20;
let totalCount;
let isLoading = false;

function loadMoreTools() {
  if (offset >= totalCount || isLoading) {
    return;
  }

  isLoading = true;
  document.getElementById("loading").classList.remove("hidden");

  fetch(`/load_more_tools?offset=${offset}&limit=${limit}`)
    .then((response) => response.json())
    .then((tools) => {
      const container = document.getElementById("tools-container");
      tools.forEach((tool) => {
        const toolElement = document.createElement("div");
        toolElement.className =
          "bg-white rounded-lg shadow-md p-6 relative cursor-pointer";
        toolElement.onclick = () => (window.location.href = `/tool/${tool.id}`);

        toolElement.innerHTML = `
                    ${
                      tool.is_loved
                        ? `
                    <div class="absolute top-2 right-2 text-red-500 animate-pulse">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                        </svg>
                    </div>
                    `
                        : ""
                    }
                    
                    <div class="flex justify-between items-start mb-4">
                        <div class="w-16 h-16 bg-gray-300 rounded-lg"></div>
                        <span class="inline-block px-2 py-1 rounded-full text-xs font-semibold ${getCategoryClass(
                          tool.category
                        )}">
                            ${tool.category || "Uncategorized"}
                        </span>
                    </div>
                    <h3 class="text-xl font-bold text-blue-800 mb-2">
                        <a href="${
                          tool.external_link
                        }" target="_blank" rel="noopener noreferrer" class="hover:underline" onclick="event.stopPropagation();">
                            ${tool.name}
                        </a>
                    </h3>
                    <p class="text-sm text-gray-700">${
                      tool.description ||
                      "A powerful tool to boost your productivity and streamline your workflow."
                    }</p>
                `;
        container.appendChild(toolElement);
      });
      offset += tools.length;
      isLoading = false;
      document.getElementById("loading").classList.add("hidden");
    });
}

function getCategoryClass(category) {
  const categoryClasses = {
    Productivity: "bg-green-200 text-green-800",
    "Project Management": "bg-blue-200 text-blue-800",
    "Creative Tools": "bg-purple-200 text-purple-800",
    Communication: "bg-yellow-200 text-yellow-800",
    Finance: "bg-red-200 text-red-800",
    Marketing: "bg-orange-200 text-orange-800",
    Analytics: "bg-indigo-200 text-indigo-800",
    "Customer Support": "bg-pink-200 text-pink-800",
    "Human Resources": "bg-teal-200 text-teal-800",
    Community: "bg-lime-200 text-lime-800",
    Education: "bg-cyan-200 text-cyan-800",
    Development: "bg-fuchsia-200 text-fuchsia-800",
    Design: "bg-rose-200 text-rose-800",
    Security: "bg-emerald-200 text-emerald-800",
  };
  return categoryClasses[category] || "bg-gray-200 text-gray-800";
}

window.addEventListener("load", () => {
  totalCount = parseInt(
    document.getElementById("total-count").dataset.totalCount
  );

  window.addEventListener("scroll", () => {
    if (
      window.innerHeight + window.scrollY >=
      document.body.offsetHeight - 100
    ) {
      loadMoreTools();
    }
  });
});
