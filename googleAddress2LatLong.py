def address2latlong(x):
    google_address = x
    index_of_at = 0
    index_of_first_comma = 0
    index_of_second_comma = 0

    for i in range(len(google_address)):
        if (google_address[i]=='@'):
            index_of_at=i
            break
    google_address = google_address[index_of_at+1:]

    for i in range(len(google_address)):
        if (google_address[i]==','):
            index_of_first_comma=i
            break
    lat = google_address[:index_of_first_comma]
    google_address = google_address[index_of_first_comma+1:]

    for i in range(len(google_address)):
        if (google_address[i]==','):
            index_of_second_comma=i
            break
    long = google_address[:index_of_second_comma]

    return lat, long

if __name__=="__main__":
    x = address2latlong("https://www.google.com/maps/@43.37433505123419,26.195611949226485,13z?hl=en-US&gl=US")
    print(x)