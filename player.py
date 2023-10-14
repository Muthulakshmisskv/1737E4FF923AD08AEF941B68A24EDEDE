class player:
  def play(self):
    print("The Player is playing cricket.")
    class Batsman(player):
      def play(self):
        print("The batsman is batting.")
        batsman=Batsman()
        bolwer=Bowler()
        batsman.play()
        bowler.play()
        