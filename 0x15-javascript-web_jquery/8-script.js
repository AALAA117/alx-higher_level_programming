$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  success: function (data) {
    const movies = data.results; movies.ForEach(function (movie) {
      $('UL#list_movies').append('<li>' + movie.name + '</li>');
    });
  }
});
