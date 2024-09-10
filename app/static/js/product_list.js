let offset = 10;
const limit = 10;
let totalCount;
let isLoading = false;

function loadMoreTools() {
    if (offset >= totalCount || isLoading) {
        return;
    }

    isLoading = true;
    document.getElementById('loading').classList.remove('hidden');

    fetch(`/load_more_tools?offset=${offset}&limit=${limit}`)
        .then(response => response.json())
        .then(tools => {
            const container = document.getElementById('tools-container');
            tools.forEach(tool => {
                const toolElement = document.createElement('div');
                toolElement.className = 'bg-white rounded-lg shadow-lg p-6';
                toolElement.innerHTML = `
                    <h3 class="text-2xl font-bold text-blue-800 mb-4">
                        <a href="/tool/${tool.id}" class="hover:underline">
                            ${tool.name}
                        </a>
                    </h3>
                    ${tool.description.slice(0, 150)}${tool.description.length > 150 ? '...' : ''}
                    <div class="flex justify-between items-center mt-4">
                        <span class="text-sm text-gray-500">Category: ${tool.category}</span>
                        <a href="/tool/${tool.id}" class="text-blue-600 hover:underline">Learn More</a>
                    </div>
                `;
                container.appendChild(toolElement);
            });
            offset += tools.length;
            isLoading = false;
            document.getElementById('loading').classList.add('hidden');
        });
}

window.addEventListener('load', () => {
    totalCount = parseInt(document.getElementById('total-count').dataset.totalCount);
    
    window.addEventListener('scroll', () => {
        if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 100) {
            loadMoreTools();
        }
    });
});