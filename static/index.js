document.addEventListener('DOMContentLoaded', function () {
    const ctxIncidence = document.getElementById('incidenceChart').getContext('2d');
    const incidenceChart = new Chart(ctxIncidence, {
        type: 'line',
        data: {
            labels: ['2015', '2016', '2017', '2018', '2019', '2020', '2021'],
            datasets: [{
                label: 'Incidence Rates',
                data: [15, 20, 25, 30, 35, 40, 50],
                borderColor: 'rgba(52, 152, 219, 1)',
                backgroundColor: 'rgba(52, 152, 219, 0.3)',
                fill: true,
                borderWidth: 2,
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Rates per 100,000',
                        color: '#34495e',
                    },
                    ticks: {
                        color: '#34495e',
                    }
                },
                x: {
                    ticks: {
                        color: '#34495e',
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        color: '#34495e',
                    }
                }
            }
        }
    });

    const ctxSurvival = document.getElementById('survivalChart').getContext('2d');
    const survivalChart = new Chart(ctxSurvival, {
        type: 'bar',
        data: {
            labels: ['2015', '2016', '2017', '2018', '2019', '2020', '2021'],
            datasets: [{
                label: 'Survival Rates',
                data: [60, 55, 53, 50, 48, 45, 40],
                backgroundColor: 'rgba(231, 76, 60, 0.7)',
                borderColor: 'rgba(231, 76, 60, 1)',
                borderWidth: 1,
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Percentage (%)',
                        color: '#34495e',
                    },
                    ticks: {
                        color: '#34495e',
                    }
                },
                x: {
                    ticks: {
                        color: '#34495e',
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        color: '#34495e',
                    }
                }
            }
        }
    });
});
