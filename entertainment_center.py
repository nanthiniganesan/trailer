import media
import fresh_tomatoes

kung_fu_panda=media.Movie("Kung fu panda","You Don’t Have to Look Like a Hero!","http://www.dreamworks.com/kungfupanda/images/uploads/games/_400/KFP3_VG_Promo_r3.jpg","https://www.youtube.com/watch?v=PXi3Mv6KMzY")

inside_out=media.Movie("Inside out","Negative Emotions Are Okay! ","https://images-na.ssl-images-amazon.com/images/M/MV5BOTgxMDQwMDk0OF5BMl5BanBnXkFtZTgwNjU5OTg2NDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=seMwpP0yeu4")

home=media.Movie("Home","Stop Judging Everyone!","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFMT_I1nC6ymOWZxik-WZRa6PttiOdMhRsywL1EzDs40fuK7MpIw","https://www.youtube.com/watch?v=MyqZf8LiWvM")


#kung_fu_panda.show_trailer()
movies=[kung_fu_panda,inside_out,home]
fresh_tomatoes.open_movies_page(movies)


