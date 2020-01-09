word = input()
print("The mystery word has " + str(len(word)) + " letters.")
tries = 0
points = 0
while True:
  guess = input()   
  tries += 1
  if len(guess) > 1:
    if guess == word:
      print("Correct!  The mystery word is " + word + ".")
      print("You made " + str(tries) + " incorrect guesses.")
      points = len(word) * 10 - tries * 5
      print("You get " + str(points) + " points.")
      break
    else:
      print("The mystery word is not " + guess + ".") 
      print("#"*6)
      print("x")
  else:
    if guess in word:
      x = ['*' for i in range(len(word))]
      for pos in range(word.count(guess)):
        x[[i for i, n in enumerate(word) if n == guess][pos]] = guess 
      show = ''.join(x) 
      print(show)
    else:
      if tries >= 10:
        print("You have no more guesses left.")
        print("You get " + str(points) + " points.")
        print("You lost the game.")
        break
      else:
        print("Incorrect!  " + guess + " is not in the word.")
