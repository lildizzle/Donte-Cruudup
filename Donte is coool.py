# Donte Crudup

media_review = []

movie = []

books = []

music = []

valid = []

Media_type = input(" What are you looking for?: ")
media_review.append(Media_type)
genre = input(" What type of gerne are you looking for?: ")

Title = input(" What is the title?: ")

Description = input(" What is it about?: ")

Year = str(input(" What year did this come out?: " ))

Rating = float(input(" What rating are you going to give this movie(1/10)?: "))


media_review = [Media_type,genre,Title,Description,Year,Rating]
print (media_review)

if Media_type == "Movie" or Media_type == "movie" or Media_type == "Flim" or Media_type == "flim":
    print (media_review)

if Media_type == "Book" or Media_type == "book" or Media_type == "Script":
    print (media_review)
    
if Media_type == "Music" or Media_type == "music" or Media_type == "Song" or Media_type == "song":
    

if Media_type == "sclupture" or Media_type  == "screen play" or Media_type == "plays":
    print (" We dont have it... sorry")
