let offset = 30; // Start with 30 since we load 30 initially
const limit = 30;
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
    .then((data) => {
      const toolsContainer = document.getElementById("tools-container");
      data.forEach((tool) => {
        const toolElement = document.createElement("div");
        toolElement.className =
          "bg-white rounded-lg shadow-md p-6 relative cursor-pointer";
        toolElement.onclick = function () {
          window.location.href = `/tool/${tool.id}`;
        };

        toolElement.innerHTML = `
          ${
            tool.is_promoted
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
              <img src="${
                tool.logo_public_url
                  ? tool.logo_public_url
                  : `https://img.logo.dev/${
                      tool.link.split("//")[1].split("/")[0]
                    }?token=${logoDevPublicKey}`
              }"
                  alt="${tool.name} logo" class="w-16 h-16 rounded-lg mr-4">
              <span class="inline-block px-2 py-1 rounded-full text-xs font-semibold 
                  ${
                    tool.ToolCategory &&
                    tool.ToolCategory.meta &&
                    tool.ToolCategory.meta.tailwindClasses
                      ? tool.ToolCategory.meta.tailwindClasses
                      : "bg-gray-200 text-gray-800"
                  }">
                  ${
                    tool.ToolCategory ? tool.ToolCategory.name : "Uncategorized"
                  }
              </span>
          </div>
          <h3 class="text-xl font-bold text-blue-800 mb-2">
              <a href="${
                tool.link
              }" target="_blank" rel="noopener noreferrer" class="hover:underline" onclick="event.stopPropagation();">
                  ${tool.name}
              </a>
          </h3>
          <p class="text-gray-700">${
            tool.description ||
            "A powerful tool to boost your productivity and streamline your workflow."
          }</p>
        `;

        toolsContainer.appendChild(toolElement);
      });

      offset += data.length; // Update the offset
      isLoading = false;
      document.getElementById("loading").classList.add("hidden");

      // Check if we've loaded all tools
      if (offset >= totalCount) {
        document.getElementById("loading").textContent = "No more tools to load";
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      isLoading = false;
      document.getElementById("loading").classList.add("hidden");
    });
}

window.addEventListener("load", () => {
  totalCount = parseInt(
    document.getElementById("total-count").dataset.totalCount
  );

  window.addEventListener("scroll", () => {
    if (
      !isLoading &&
      window.innerHeight + window.scrollY >= document.body.offsetHeight - 100
    ) {
      loadMoreTools();
    }
  });
});
