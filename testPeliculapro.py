import unittest
import Peliculapro

class TestInsert(unittest.TestCase):

	def setUp(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()

	def tearDown(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()

	def test_insertarPelicula(self):
		#Insertar Correcto
		pelicula = Peliculapro.Pelicula('c207267u99', 'La nueva Cenicienta', 'Comedy, Musical', '1964', 'N/A', '5.9', 'Antonio, the famous dancer is preparing a big performance for the TV. But he is missing a good female dancer. One day he sees a girl dancing in the streets but when he is going to talk to ...', 'https://www.youtube.com/watch?v=Cb4-aUqfeCM', 'La Nueva Cenicienta 2', 'www.cinecalidad.com')
		resultado = Peliculapro.Sqlitedb.insertarPelicula(self, pelicula)
		self.assertEqual(resultado, [('c207267u99', 'La nueva Cenicienta', 'Comedy, Musical', '1964', 'N/A', '5.9', 'Antonio, the famous dancer is preparing a big performance for the TV. But he is missing a good female dancer. One day he sees a girl dancing in the streets but when he is going to talk to ...', 'https://www.youtube.com/watch?v=Cb4-aUqfeCM', 'La Nueva Cenicienta 2', 'www.cinecalidad.com')])
		#No se puede insertar
		res2 = Peliculapro.Sqlitedb.insertarPelicula(self, "laudantium enim quasi")
		self.assertEqual(res2, "No se pudo agregar la pelicula a la tabla, probablemente no está en la api")

class TestDelete(unittest.TestCase):
	def setUp(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt2381941', 'Focus', 'Comedy, Crime, Drama, Romance', '27 Feb 2015', 'https://m.media-amazon.com/images/M/MV5BMTUwODg2OTA4OF5BMl5BanBnXkFtZTgwOTE5MTE4MzE@._V1_SX300.jpg', '6.6', 'In the midst of veteran con man Nickys latest scheme, a woman from his past - now an accomplished femme fatale - shows up and throws his plans for a loop.', 'https://www.youtube.com/watch?v=230wTfxE1VE', 'Ninguna', 'www.lashorasperdidas.com')""")
		conn.commit()
		conn.close()

	def tearDown(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()


	def test_eliminarPelicula(self):
		#No se puede eliminar, el ID no es el correspondiente
		pelicula = Peliculapro.Pelicula('9898989', 'Focus', 'Comedy, Crime, Drama, Romance', '27 Feb 2015', 'https://m.media-amazon.com/images/M/MV5BMTUwODg2OTA4OF5BMl5BanBnXkFtZTgwOTE5MTE4MzE@._V1_SX300.jpg', '6.6', 'In the midst of veteran con man Nickys latest scheme, a woman from his past - now an accomplished femme fatale - shows up and throws his plans for a loop.', 'https://www.youtube.com/watch?v=230wTfxE1VE', 'Ninguna', 'www.lashorasperdidas.com')
		resultado = Peliculapro.Sqlitedb.eliminarPelicula(self, pelicula)
		self.assertEqual(resultado, "No se puede eliminar la película porque no está en la base de datos")
		#No se puede eliminar, no hay id para comparar
		resultado2 = Peliculapro.Sqlitedb.eliminarPelicula(self, None)
		self.assertEqual(resultado, "No se puede eliminar la película porque no está en la base de datos")
		#Se elimina con exito, si se encuentra el Id
		"""pelicula2 = Peliculapro.Pelicula('tt2381941', 'Focus', 'Comedy, Crime, Drama, Romance', '27 Feb 2015', 'https://m.media-amazon.com/images/M/MV5BMTUwODg2OTA4OF5BMl5BanBnXkFtZTgwOTE5MTE4MzE@._V1_SX300.jpg', '6.6', 'In the midst of veteran con man Nickys latest scheme, a woman from his past - now an accomplished femme fatale - shows up and throws his plans for a loop.', 'https://www.youtube.com/watch?v=230wTfxE1VE', 'Ninguna', 'www.lashorasperdidas.com')
		resultado3 = Peliculapro.Sqlitedb.eliminarPelicula(self, pelicula2)
		self.assertEqual(resultado, "Se ha eliminado con éxito la pelicula Focus")"""

class TestUpdate(unittest.TestCase):

	def setUp(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt1657507', 'Colombiana', 'Action, Crime, Drama, Thriller', '26 Aug 2011', 'https://m.media-amazon.com/images/M/MV5BMTM0NDI2NjgxNl5BMl5BanBnXkFtZTcwMTYyNjA3NQ@@._V1_SX300.jpg', '6.4', 'A young woman, rows up to be a stone-cold assassin.', 'https://www.youtube.com/watch?v=myO2vmvggas', 'Ninguna', 'www.elmulticine.com')""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt2171665', 'Violetta', 'Drama, Family, Music, Romance', '14 May 2012', 'https://m.media-amazon.com/images/M/MV5BZmM1MWNmZDMtYzZjOC00YjExLWIyMWItYjE4ZTlmOGUwYWJhXkEyXkFqcGdeQXVyNDU2Mzg5MTM@._V1_SX300.jpg', '5.3', 'A musically talented teenager who returns to her native Buenos Aires after living in Europe.', Null, Null, Null)""")
		conn.commit()
		conn.close()

	def tearDown(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()

	def test_agregarLink(self):
		#La pelicula no está en la bd, error al actualizar
		pelicula = Peliculapro.Pelicula('tt17', 'Colombiana', 'Action, Crime, Drama, Thriller', '26 Aug 2011', 'https://m.media-amazon.com/images/M/MV5BMTM0NDI2NjgxNl5BMl5BanBnXkFtZTcwMTYyNjA3NQ@@._V1_SX300.jpg', '6.4', 'A young woman, rows up to be a stone-cold assassin.', 'https://www.youtube.com/watch?v=myO2vmvggas', 'Ninguna', 'www.elmulticine.com')
		resultado = Peliculapro.Sqlitedb.agregarLink(self, pelicula, "https://www.youtube.com/watch?v=kiZEdN98F7c")
		self.assertEqual(resultado, "No se puede actualizar el link de la película porque no está en la base de datos")
		#No se puede actualizar porque existe el registro
		resultado2 = Peliculapro.Sqlitedb.agregarLink(self, None, "https://www.youtube.com/watch?v=kiZEdN98F7c")
		self.assertEqual(resultado2, "No se puede actualizar el link de la película porque no está en la base de datos")
		#Link actualizado
		pelicula2 = Peliculapro.Pelicula('tt1657507', 'Colombiana', 'Action, Crime, Drama, Thriller', '26 Aug 2011', 'https://m.media-amazon.com/images/M/MV5BMTM0NDI2NjgxNl5BMl5BanBnXkFtZTcwMTYyNjA3NQ@@._V1_SX300.jpg', '6.4', 'A young woman, rows up to be a stone-cold assassin.', 'https://www.youtube.com/watch?v=myO2vmvggas', 'Ninguna', 'www.elmulticine.com')
		resultado3 = Peliculapro.Sqlitedb.agregarLink(self, pelicula2, "https://www.elmulticine.com/trailers2.php?orden=9010")
		self.assertEqual(resultado3, [('tt1657507', 'Colombiana', 'Action, Crime, Drama, Thriller', '26 Aug 2011', 'https://m.media-amazon.com/images/M/MV5BMTM0NDI2NjgxNl5BMl5BanBnXkFtZTcwMTYyNjA3NQ@@._V1_SX300.jpg', '6.4', 'A young woman, rows up to be a stone-cold assassin.', 'https://www.youtube.com/watch?v=myO2vmvggas', 'Ninguna', 'https://www.elmulticine.com/trailers2.php?orden=9010')])
		#Datos incompletos
		pelicula3 = Peliculapro.Pelicula('tt2171665', 'Violetta', 'Drama, Family, Music, Romance', '14 May 2012', 'https://m.media-amazon.com/images/M/MV5BZmM1MWNmZDMtYzZjOC00YjExLWIyMWItYjE4ZTlmOGUwYWJhXkEyXkFqcGdeQXVyNDU2Mzg5MTM@._V1_SX300.jpg', '5.3', 'A musically talented teenager who returns to her native Buenos Aires after living in Europe.', None, None, None)
		resultado4 = Peliculapro.Sqlitedb.agregarLink(self, pelicula3, "https://www.youtube.com/watch?v=UgvsZ-XLHS0")
		self.assertEqual(resultado4, [('tt2171665', 'Violetta', 'Drama, Family, Music, Romance', '14 May 2012', 'https://m.media-amazon.com/images/M/MV5BZmM1MWNmZDMtYzZjOC00YjExLWIyMWItYjE4ZTlmOGUwYWJhXkEyXkFqcGdeQXVyNDU2Mzg5MTM@._V1_SX300.jpg', '5.3', 'A musically talented teenager who returns to her native Buenos Aires after living in Europe.', None, None, 'https://www.youtube.com/watch?v=UgvsZ-XLHS0')])

class TestSelect(unittest.TestCase):

	def setUp(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt0475293', 'High School Musical', 'Comedy, Drama, Family, Music, Musical, Romance', '20 Jan 2006', 'https://m.media-amazon.com/images/M/MV5BZmQ3MXkFqcGdeQXVyMTczNjQwOTY@._V1_SX300.jpg', '5.3', 'A popular high school athlete and an academically gifted girl get roles in the school musical and develop a friendship', 'https://www.youtube.com/watch?v=ukDLkkvZYFk', 'HSM2, HSM3, HSM EL DESAFIO', 'www.cinecalidad.com')""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt0810900', 'High School Musical 2', 'Comedy, Drama, Family, Music, Musical, Romance', '17 Aug 2007', 'https://m.media-amazon.com/images/M/MV5kFtZTgwMDg3ODYzMjE@._V1_SX300.jpg', '9.4', 'The East High Wildcats are ready to make it the time of their lives', Null, Null, Null)""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt0962726', 'High School Musical 3: Senior Year', 'Comedy, Drama, Family, Music, Musical, Romance', '24 Oct 2008', 'https://m.media-amazon.com/images/M/MV5BNDE1NjU2wMTg3NDA3MQ@@._V1_SX300.jpg', '7.4', 'Troy and Gabriella struggle with the idea of being separated from one another as college approaches.', 'https://www.youtube.com/watch?v=bEQXcbqvbT0', 'HSM1, HSM2, HSM EL DESAFIO', 'www.cinecalidad.com')""")
		conn.commit()
		conn.close()

	def tearDown(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()

	def test_consultarPelicula(self):
		#Select de pelicula existente
		pelicula = Peliculapro.Pelicula('tt0962726', 'High School Musical 3: Senior Year', 'Comedy, Drama, Family, Music, Musical, Romance', '24 Oct 2008', 'https://m.media-amazon.com/images/M/MV5BNDE1NjU2wMTg3NDA3MQ@@._V1_SX300.jpg', '7.4', 'Troy and Gabriella struggle with the idea of being separated from one another as college approaches.', 'https://www.youtube.com/watch?v=bEQXcbqvbT0', 'HSM1, HSM2, HSM EL DESAFIO', 'www.cinecalidad.com')
		resultado = Peliculapro.Sqlitedb.consultarPelicula(self, pelicula)
		self.assertEqual(resultado, [('tt0962726', 'High School Musical 3: Senior Year', 'Comedy, Drama, Family, Music, Musical, Romance', '24 Oct 2008', 'https://m.media-amazon.com/images/M/MV5BNDE1NjU2wMTg3NDA3MQ@@._V1_SX300.jpg', '7.4', 'Troy and Gabriella struggle with the idea of being separated from one another as college approaches.', 'https://www.youtube.com/watch?v=bEQXcbqvbT0', 'HSM1, HSM2, HSM EL DESAFIO', 'www.cinecalidad.com')])
		#Select de registro inexistente
		resultado2 = Peliculapro.Sqlitedb.consultarPelicula(self, None)
		self.assertEqual(resultado2, "La película que buscas no está en la base de datos")
		#Select con id modificado, id se compara y genera error
		pelicula2 = Peliculapro.Pelicula('911', 'High School Musical', 'Comedy, Drama, Family, Music, Musical, Romance', '20 Jan 2006', 'https://m.media-amazon.com/images/M/MV5BZmQ3MXkFqcGdeQXVyMTczNjQwOTY@._V1_SX300.jpg', '5.3', 'A popular high school athlete and an academically gifted girl get roles in the school musical and develop a friendship', 'https://www.youtube.com/watch?v=ukDLkkvZYFk', 'HSM2, HSM3, HSM EL DESAFIO', 'www.cinecalidad.com')
		resultado3 = Peliculapro.Sqlitedb.consultarPelicula(self, pelicula2)
		self.assertEqual(resultado3, "La película que buscas no está en la base de datos")

		pelicula3 = Peliculapro.Pelicula('tt0810900', 'High School Musical 2', 'Comedy, Drama, Family, Music, Musical, Romance', '17 Aug 2007', 'https://m.media-amazon.com/images/M/MV5kFtZTgwMDg3ODYzMjE@._V1_SX300.jpg', '9.4', 'The East High Wildcats are ready to make it the time of their lives', None, None, None)
		resultado4 = Peliculapro.Sqlitedb.consultarPelicula(self, pelicula3)
		self.assertEqual(resultado4, [('tt0810900', 'High School Musical 2', 'Comedy, Drama, Family, Music, Musical, Romance', '17 Aug 2007', 'https://m.media-amazon.com/images/M/MV5kFtZTgwMDg3ODYzMjE@._V1_SX300.jpg', '9.4', 'The East High Wildcats are ready to make it the time of their lives', None, None, None)])

class TestGetSqlite(unittest.TestCase):

	def setUp(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt0475293', 'High School Musical', 'Comedy, Drama, Family, Music, Musical, Romance', '20 Jan 2006', 'https://m.media-amazon.com/images/M/MV5BZmQ3MXkFqcGdeQXVyMTczNjQwOTY@._V1_SX300.jpg', '5.3', 'A popular high school athlete and an academically gifted girl get roles in the school musical and develop a friendship', 'https://www.youtube.com/watch?v=ukDLkkvZYFk', 'HSM2, HSM3, HSM EL DESAFIO', 'www.cinecalidad.com')""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt0810900', 'High School Musical 2', 'Comedy, Drama, Family, Music, Musical, Romance', '17 Aug 2007', 'https://m.media-amazon.com/images/M/MV5kFtZTgwMDg3ODYzMjE@._V1_SX300.jpg', '9.4', 'The East High Wildcats are ready to make it the time of their lives', Null, Null, Null)""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt0962726', 'High School Musical 3: Senior Year', 'Comedy, Drama, Family, Music, Musical, Romance', '24 Oct 2008', 'https://m.media-amazon.com/images/M/MV5BNDE1NjU2wMTg3NDA3MQ@@._V1_SX300.jpg', '7.4', 'Troy and Gabriella struggle with the idea of being separated from one another as college approaches.', 'https://www.youtube.com/watch?v=bEQXcbqvbT0', 'HSM1, HSM2, HSM EL DESAFIO', 'www.cinecalidad.com')""")
		conn.commit()
		conn.close()

	def tearDown(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()

	def test_get_pelicula(self):
		res = Peliculapro.Sqlitedb.get_pelicula(self, "High School Musical")
		pelicula = Peliculapro.Pelicula('tt0475293', 'High School Musical', 'Comedy, Drama, Family, Music, Musical, Romance', '20 Jan 2006', 'https://m.media-amazon.com/images/M/MV5BZmQ3MXkFqcGdeQXVyMTczNjQwOTY@._V1_SX300.jpg', '5.3', 'A popular high school athlete and an academically gifted girl get roles in the school musical and develop a friendship', 'https://www.youtube.com/watch?v=ukDLkkvZYFk', 'HSM2, HSM3, HSM EL DESAFIO', 'www.cinecalidad.com')
		self.assertEqual(res.id, pelicula.id)

		res2 = Peliculapro.Sqlitedb.get_pelicula(self, "High")
		self.assertEqual(res2, None)

		res3 = Peliculapro.Sqlitedb.get_pelicula(self, 'High School Musical 2')
		pelicula2 = Peliculapro.Pelicula('tt0810900', 'High School Musical 2', 'Comedy, Drama, Family, Music, Musical, Romance', '17 Aug 2007', 'https://m.media-amazon.com/images/M/MV5kFtZTgwMDg3ODYzMjE@._V1_SX300.jpg', '9.4', 'The East High Wildcats are ready to make it the time of their lives', None, None, None)
		self.assertEqual(res3.id, pelicula2.id)

class TestGetOMDBApi(unittest.TestCase):

	def setUp(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt0475293', 'High School Musical', 'Comedy, Drama, Family, Music, Musical, Romance', '20 Jan 2006', 'https://m.media-amazon.com/images/M/MV5BZmQ3MXkFqcGdeQXVyMTczNjQwOTY@._V1_SX300.jpg', '5.3', 'A popular high school athlete and an academically gifted girl get roles in the school musical and develop a friendship', 'https://www.youtube.com/watch?v=ukDLkkvZYFk', 'HSM2, HSM3, HSM EL DESAFIO', 'www.cinecalidad.com')""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt0810900', 'High School Musical 2', 'Comedy, Drama, Family, Music, Musical, Romance', '17 Aug 2007', 'https://m.media-amazon.com/images/M/MV5kFtZTgwMDg3ODYzMjE@._V1_SX300.jpg', '9.4', 'The East High Wildcats are ready to make it the time of their lives', Null, Null, Null)""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt0962726', 'High School Musical 3: Senior Year', 'Comedy, Drama, Family, Music, Musical, Romance', '24 Oct 2008', 'https://m.media-amazon.com/images/M/MV5BNDE1NjU2wMTg3NDA3MQ@@._V1_SX300.jpg', '7.4', 'Troy and Gabriella struggle with the idea of being separated from one another as college approaches.', 'https://www.youtube.com/watch?v=bEQXcbqvbT0', 'HSM1, HSM2, HSM EL DESAFIO', 'www.cinecalidad.com')""")
		conn.commit()
		conn.close()

	def tearDown(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()

	def test_get_pelicula(self):
		api = Peliculapro.OmdbApi()
		res = Peliculapro.OmdbApi.get_pelicula(api, "High School Musical")
		pelicula = Peliculapro.Pelicula('tt0475293', 'High School Musical', 'Comedy, Drama, Family, Music, Musical, Romance', '20 Jan 2006', 'https://m.media-amazon.com/images/M/MV5BZmQ3MXkFqcGdeQXVyMTczNjQwOTY@._V1_SX300.jpg', '5.3', 'A popular high school athlete and an academically gifted girl get roles in the school musical and develop a friendship', 'https://www.youtube.com/watch?v=ukDLkkvZYFk', 'HSM2, HSM3, HSM EL DESAFIO', 'www.cinecalidad.com')
		self.assertEqual(res.id, pelicula.id)
		res2 = Peliculapro.OmdbApi.get_pelicula(api, "HSM-3")
		self.assertEqual(res2, "No se encontró la pelicula en la Api")
		res3 = Peliculapro.OmdbApi.get_pelicula(api, "Tangled")
		pelicula2 = Peliculapro.Pelicula('tt0398286', 'Tangled', 'Animation, Adventure, Comedy, Family, Fantasy, Musical, Romance', '24 Nov 2010', 'https://m.media-amazon.com/images/M/MV5BMTAxNDYxMjg0MjNeQTJeQWpwZ15BbWU3MDcyNTk2OTM@._V1_SX300.jpg', '7.8', 'The magically long-haired Rapunzel has spent her entire life in a tower, but now that a runaway thief has stumbled upon her, she is about to discover the world for the first time, and who she really is.', None, None, None)
		self.assertEqual(res3.id, pelicula2.id)

if __name__ == '__main__':
	unittest.main()
