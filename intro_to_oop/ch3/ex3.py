class Candidate:

    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        
        self.votes = self.votes + other
        return self
    
    def get_name(self):
        return self.name
    
    def get_votes(self):
        return self.votes

class Election:

    def __init__(self, candidates):
        self.candidates = candidates

    def determine_winner(self):
        winning_tally = 0
        winner = None

        for candidate in self.candidates:
            if candidate.votes > winning_tally:
                winning_tally = candidate.votes
                winner = candidate.name
        
        return winner, winning_tally
    
    def total_votes(self):
        total_votes = 0

        for candidate in self.candidates:
            total_votes += candidate.votes

        return total_votes

    def results(self):
        winner, winning_tally = self.determine_winner()
        total_votes = self.total_votes()
        winning_percentage = (winning_tally / self.total_votes()) * 100

        for candidate in self.candidates:
            if candidate.get_votes() == 1:
                print(f'{candidate.get_name()}: {candidate.get_votes()}  vote')
            else:
                print(f'{candidate.get_name()}: {candidate.get_votes()}  votes')

        print(f'{winner} won: {winning_percentage:.1f}% of the votes')

        return None

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()