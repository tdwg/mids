// Mappings Table Filters

		let allData = [];
        let filteredData = [];

        // Fetch data and filters when page loads
        window.addEventListener('DOMContentLoaded', async () => {
            await loadFilters();
            await loadData();
            setupEventListeners();
        });

        // Load filter options from Flask backend
        async function loadFilters() {
            try {
                const response = await fetch('/api/filters.json');
                const filters = await response.json();

                // Populate level dropdown
                const levelSelect = document.getElementById('levelFilter');
                filters.levels.forEach(lvl => {
                    const option = document.createElement('option');
                    option.value = lvl;
                    option.textContent = lvl;
                    levelSelect.appendChild(option);
                });

                // Populate position dropdown
                const infoElementSelect = document.getElementById('infoElementFilter');
                filters.infoElements.forEach(infoEle => {
                    const option = document.createElement('option');
                    option.value = infoEle;
                    option.textContent = infoEle;
                    infoElementSelect.appendChild(option);
                });
            } catch (error) {
                console.error('Error loading filters:', error);
            }
        }

        // Load table data from Flask backend
        async function loadData() {
            try {
                const response = await fetch('/api/data.json');
                allData = await response.json();
                filteredData = [...allData];
                renderTable();
                updateStats();
            } catch (error) {
                console.error('Error loading data:', error);
                document.getElementById('tableBody').innerHTML =
                    '<tr><td colspan="5" class="no-results">Error loading data. Please refresh the page.</td></tr>';
            }
			console.log(allData)
        }

        // Setup event listeners for filters
        function setupEventListeners() {
            document.getElementById('levelFilter').addEventListener('change', filterTable);
            document.getElementById('infoElementFilter').addEventListener('change', filterTable);
            document.getElementById('termFilter').addEventListener('input', filterTable);
			document.getElementById('namespaceFilter').addEventListener('change', filterTable);
        }

        // Filter table based on selected criteria
        function filterTable() {
            const levelFilter = document.getElementById('levelFilter').value.toLowerCase();
            const infoElementFilter = document.getElementById('infoElementFilter').value.toLowerCase();
            const termFilter = document.getElementById('termFilter').value.toLowerCase();
			const namespaceFilter= document.getElementById('namespaceFilter').value.toLowerCase();

            filteredData = allData.filter(item => {
				console.log(item)
                const matchesLevel = !levelFilter || item.sssom_subject_category.toLowerCase() === levelFilter;
                const matchesInfoElement = !infoElementFilter || item.sssom_subject_id.toLowerCase() === infoElementFilter;
                const matchesTerm = !termFilter || item.sssom_object_id.toLowerCase().includes(termFilter);
				const matchesNamespace = !namespaceFilter || item.object_namespace.toLowerCase().includes(namespaceFilter);

                return matchesLevel && matchesInfoElement && matchesTerm && matchesNamespace;
            });

            renderTable();
            updateStats();
        }

        // Render the table with current filtered data
        function renderTable() {
            const tbody = document.getElementById('tableBody');

            if (filteredData.length === 0) {
                tbody.innerHTML = '<tr><td colspan="5" class="no-results">No results found. Try adjusting your filters.</td></tr>';
                return;
            }

            tbody.innerHTML = filteredData.map(item => `
                <tr>
                    <td data-th="Subject Category: ">${item.sssom_subject_category}</td>
                    <td data-th="Subject ID: ">${item.sssom_subject_id}</td>
                    <td data-th="Object Category: ">${item.sssom_object_category}</td>
                    <td data-th="Object ID: ">${item.sssom_object_id}</td>
                    <td class="indicator-td"><i class="fa"></i> </td>
                </tr>
            `).join('');
        }



        // Update statistics display
        function updateStats() {
            const stats = document.getElementById('stats');
            stats.textContent = `Showing ${filteredData.length} of ${allData.length} employees`;
        }

        // Reset all filters
        function resetFilters() {
            document.getElementById('levelFilter').value = '';
            document.getElementById('infoElementFilter').value = '';
            document.getElementById('termFilter').value = '';
            filterTable();
        }