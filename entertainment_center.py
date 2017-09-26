import media
import fresh_tomatoes

cars = media.Movie("Cars",
                   '''A hot-shot race-car named Lightning McQueen gets waylaid
in Radiator Springs, where he finds the true meaning of friendship
and family.''',
                   '''https://images-na.ssl-images-amazon.com/images/M/MV5BMTg5N
zY0MzA2MV5BMl5BanBnXkFtZTYwNDc3NTc2._V1_QL50_.jpg''',
                   '''https://www.youtube.com/watch?v=WGByijP0Leo''')
# Creating object 1

bvs = media.Movie("Batman Vs. Superman",
                  '''Fearing that the actions of Superman are left unchecked,
Batman takes on the Man of Steel, while the world wrestles with what kind of a
hero it really needs.''',
                  '''https://images-na.ssl-images-amazon.com/images/M/MV5BYThjY
zcyYzItNTVjNy00NDk0LTgwMWQtYjMwNmNlNWJhMzMyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_QL5
0_SY1000_CR0,0,675,1000_AL_.jpg''',
                  '''https://www.youtube.com/watch?v=fis-9Zqu2Ro''')
# Creating object 2

boss_baby = media.Movie("Boss Baby",
                        '''A suit-wearing, briefcase-carrying baby pairs up with
his 7-year old brother to stop the dastardly plot of the
CEO of Puppy Co.''',
                        '''https://images-na.ssl-images-amazon.com/images/M/MV5B
MTk2NjI5NzgwNl5BMl5BanBnXkFtZTgwNDc4NTA1OTE@._V1_QL50_SY1000_CR0,0,947,1000_AL_.
jpg''',
                        '''https://www.youtube.com/watch?v=h24gEn3y82Q''')
# Creating object 3

thor2 = media.Movie("Thor: The Dark World",
                    '''When Dr. Jane Foster gets cursed with a powerful entity
known as the Aether, Thor is heralded of the cosmic event known as the
Convergence and the genocidal Dark Elves.''',
                    '''https://images-na.ssl-images-amazon.com/images/M/MV5BMTQy
NzAwOTUxOF5BMl5BanBnXkFtZTcwMTE0OTc5OQ@@._V1_QL50_SY1000_SX700_AL_.jpg''',
                    '''https://www.youtube.com/watch?v=npvJ9FTgZbM''')
# Creating object 4

avengers2 = media.Movie("Avengers: Age of Ultron",
                        '''When Tony Stark and Bruce Banner try to jump-start a
dormant peacekeeping program called Ultron, things go horribly wrong and it's
up to Earth's mightiest heroes to stop the villainous Ultron from enacting his
terrible plan.''',
                        '''https://images-na.ssl-images-amazon.com/images/M/MV5B
MTM4OGJmNWMtOTM4Ni00NTE3LTg3MDItZmQxYjc4N2JhNmUxXkEyXkFqcGdeQXVyNTgzMDMzMTg@._V1
_QL50_SY1000_SX675_AL_.jpg''',
                        '''https://www.youtube.com/watch?v=rD8lWtcgeyg''')
# Creating object 5

johnwick2 = media.Movie("John Wick: Chapter 2",
                        '''After returning to the criminal underworld to repay a
debt, John Wick discovers that a large bounty has been put on his life.''',
                        '''https://images-na.ssl-images-amazon.com/images/M/MV5B
MjE2NDkxNTY2M15BMl5BanBnXkFtZTgwMDc2NzE0MTI@._V1_QL50_SY1000_CR0,0,648,1000_AL_
.jpg''',
                        '''https://www.youtube.com/watch?v=XGk2EfbD_Ps''')
# Creating object 6

movies = [cars, bvs, boss_baby,
          thor2, avengers2, johnwick2]  # list to store all the movie titles

fresh_tomatoes.open_movies_page(movies)
# calling the html with the movie list as argument
