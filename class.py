
class paciente:
    def __init__(self, nome, exame, data, hora):
        self._nome = nome
        self._exame = exame
        self._data = data
        self._hora = hora

    def _get_nome(self):
        return self._nome
    def _set_nome(self, nome):
        self._nome = nome
    def _get__cod(self):
        return self._cod
    def _set__cod(self, cod):
        self._cod = _cod
    def _get__exame(self):
        return self._exame
    def _set__exame(self, exame):
        self.__exame = _exame
    def _get_data(self):
        return self._data
    def _set_data(self, data):
        self._data = data
    def _get_hora(self):
        return self._hora
    def _set_hora(self, hora):
        self._hora = hora
    nome = property( _get_nome, _set_nome)

p = Paciente('Julio', 'consulta','10/10/2019','12:10')
print (p._get_nome())
