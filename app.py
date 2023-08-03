from classes.dojo_pets import Ninja, Pet

pet = Pet("Kirby", "Big Boy", "Jump")
pet.stats()
pet.sleep()
pet.stats()
pet.eat()
pet.stats()
pet.noise()
pet.stats()
pet.play()
pet.stats()


paul = Ninja("Paul", "De Ulloa", "jerky", "chicken", pet)
paul.walk().feed().bathe()
