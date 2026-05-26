let seriesContainer = document.querySelector('.series-list');
let moviesContainer = document.querySelector('.movies-list');
let uploadContainer = document.querySelector('.upload');

function showSeriesList() {
     seriesContainer.style.display = 'flex';
     moviesContainer.style.display = 'none';
     uploadContainer.style.display = 'none';
}

function showMoviesList() {
     seriesContainer.style.display = 'none';
     moviesContainer.style.display = 'flex';
     uploadContainer.style.display = 'none';
}

function showUploadContainer() {
     seriesContainer.style.display = 'none';
     moviesContainer.style.display = 'none';
     uploadContainer.style.display = 'flex';
}

showUploadContainer()
