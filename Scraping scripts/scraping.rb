require 'open-uri'
require 'nokogiri'
require 'csv'

a = []

price = []
address = []
area = []
persqft = []
room = []
bathroom = []
verify = []
floor = []
community = []
power = []
secure = []

100.times do |i|
	url = ""	#Enter URL here
	page = Nokogiri::HTML(open(url))

	page.css('div.listing_list div.listing_list__content div.listing__title div.result__details__price').each do |line|
		price << line.text.strip.split(/ \n /)
	end

	page.css('div.listing_list div.listing_list__content div.listing__title div.listing__title__text').each do |line|
		address << line.text.strip.split(/ \n /)
	end

	page.css('div.listing_list div.listing_list__content div.listing__keywords span.summary-item.size').each do |line|
		area << line.text.strip.split(/ \n /)
	end

	page.css('div.listing_list div.listing_list__content div.listing__keywords span.summary-item.size-per').each do |line|
		persqft << line.text.strip.split(/ \n /)
	end

	page.css('div.listing_list div.listing_list__content div.listing__keywords span.summary-item.rooms').each do |line|
		room << line.text.strip.split(/ \n /)
	end

	page.css('div.listing_list div.listing_list__content div.listing__keywords span.summary-item.bathrooms').each do |line|
		bathroom << line.text.strip.split(/ \n /)
	end

	page.css('div.listing_list div.listing_list__content div.listing__keywords span.summary-item.property_verified').each do |line|
		verify << line.text.strip.split(/ \n /)
	end

	page.css('div.listing_list div.listing_list__content div.listing__keywords span.summary-item.independent_floor').each do |line|
		floor << line.text.strip.split(/ \n /)
	end

	page.css('div.listing_list div.listing_list__content div.listing__keywords span.summary-item.gated').each do |line|
		community << line.text.strip.split(/ \n /)
	end

	page.css('div.listing_list div.listing_list__content div.listing__keywords span.summary-item.power_backup').each do |line|
		power << line.text.strip.split(/ \n /)
	end

	page.css('div.listing_list div.listing_list__content div.listing__keywords span.summary-item.security').each do |line|
		secure << line.text.strip.split(/ \n /)
	end
end

CSV.open("h.csv", "w") do |file|
	file << ["Price", "Address", "Area", "Per_Square_Price", "Room", "Bathroom", "Verified?", "Floor", "Community", "Power_Backup", "Security"]

	price.length.times do |i|
		file << [price[i], address[i], area[i], persqft[i], room[i], bathroom[i], verify[i], floor[i], community[i], power[i], secure[i]]
	end
end
