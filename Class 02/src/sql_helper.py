

def create_sql_count_artists_in_chinook():
    return """SELECT count (artistid) FROM artist"""

def create_sql_count_orders_in_cities():
    return """SELECT Invoice.BillingCity, COUNT(*) AS Invoice_amount FROM Invoice GROUP BY Invoice.BillingCity 
    ORDER BY Invoice_amount DESC;"""

def create_sql_protected_aac_audio_file():
    return """SELECT COUNT(*) FROM Track JOIN MediaType ON Track.MediaTypeId=MediaType.MediaTypeId 
    WHERE MediaType.Name='Protected AAC audio file';"""

def create_sql_artist_most_albums():
    return """SELECT Artist.Name, COUNT(*) as Album_amount FROM Artist JOIN Album ON Album.ArtistId = Artist.ArtistId
    GROUP BY Album.ArtistId ORDER BY Album_amount DESC;"""

def create_sql_genre_most_tracks():
    return """SELECT Genre.Name, COUNT(*) as Track_amount FROM Genre JOIN Track ON Track.GenreId = Genre.GenreId
    GROUP BY Track.GenreId ORDER BY Track_amount DESC;"""

def create_sql_customer_most_money():
    return """SELECT Customer.FirstName, Customer.LastName, SUM(Invoice.Total) AS Invoice_total FROM Customer 
    JOIN Invoice ON Invoice.CustomerId = Customer.CustomerId GROUP BY Invoice.CustomerId ORDER BY Invoice_total DESC;"""

def create_sql_songs_with_each_order():
    return """SELECT Invoice.InvoiceId, Track.Name FROM Invoice JOIN InvoiceLine 
    ON InvoiceLine.InvoiceId = Invoice.InvoiceId JOIN Track ON InvoiceLine.TrackId = Track.TrackId;"""
