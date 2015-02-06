    test = [1, 2, 3, 4]
    for value in test
        next if value%2 == 0
        puts value
    end


=start
Two (Make that three) ways to write a loop, the second is my ruby-tastic.
=end


# This is number one
stops = ["East Bumpspark", "Endertromb Avenue", "New Mixico", "Mal
Abochny"]
for stop in stops
 next if stop.empty?
end


# Number two
stops = ["East Bumpspark", "Endertromb Avenue", "New Mixico",
"Mal Abochny"]
stops.each do |stop|
 next if stop.empty?
end

# Number three
stops = ["East Bumpspark", "Endertromb Avenue", "New Mixico",
"Mal Abochny"]
stops.each { |stop| next if stop.empty? }