var app = new Vue({
  el: '#app',
  data: {
    endpoint: 'http://localhost:8080/personaje',
    nombre: '',
    apellido: '',
    twitter: '',
    numero: 0,
    imagen_visible: true,
    personajes: []
  },
  methods: {
    reload: function() {
        this.$http.get(this.endpoint).then(function(response){
        console.log('Respuesta del servidor: ' + response);
        this.personajes = response.body;
      }, function(){
        alert('Error on load!');
      });
    },
    save: function() {
        this.$http.post(this.endpoint, {
            "first_name": this.nombre,
            "last_name": this.apellido,
            "twitter": this.twitter,
        }).then(function(response){
        console.log('Respuesta del servidor: ' + response);
        this.personajes = response.body;
      }, function(){
        alert('Error on save!');
      });
    }
  }
});

