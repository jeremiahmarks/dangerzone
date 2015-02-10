

* start game
	while there are still more than one players
		get new deck of cards
		clear players hands of cards
		for each player
			attempt to collect ante
			if unable to collect ante
				remove player from table.

		deal each player one card facedown and then one card faceup

		until there are no more "hits"
			ask each player what their plan is
			if it is hit
				deal card faceup to player

		calculate winner
			if only one person has 21
				give them pot and announce winner
			elif multiple people have 21
				split up pot evenly and distribute
			elif only one person has stand
				give them pot and announce winner
			elif multiple people have stand
				find the person/people closest to 21
				split up pot evenly and distribute
		set pot=0
		clear players hands of cards

		complete anteCheck
			if player unable to meet ante
				remove them from table
