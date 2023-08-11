import sys
import requests

# Define a function to filter and save URLs
# URL'leri filtrelemek ve kaydetmek için bir fonksiyon tanımla

def urls(out_file):
    # Read URLs from standard input and split them into lines
    # URL'leri standart girdiden oku ve satırlara ayır

    url2 = sys.stdin.read().splitlines()

    # Lists to store good and bad URLs
    # İyi ve kötü URL'leri depolamak için listeler

    good_urls = []
    bad_urls = []

    # Iterate through each URL
    # Her bir URL üzerinde döngü kur

    for url in url2:
        try:
            # Send a HEAD request to the URL
            # URL'ye bir HEAD isteği gönder

            response = requests.head(url)

            # Check if the response status code is 200 (OK)
            # Yanıt durum kodunun 200 (Tamam) olup olmadığını kontrol et

            if response.status_code == 200:
                good_urls.append(url)  # Add the URL to the list of good URLs
                                       # URL'yi iyi URL'ler listesine ekle

        except requests.exceptions.MissingSchema:
            bad_urls.append(url)  # If there's a MissingSchema exception, add the URL to the list of bad URLs
            continue              # Eğer bir MissingSchema istisnası oluşursa, URL'yi kötü URL'ler listesine ekle
        except requests.exceptions.ConnectionError:
            bad_urls.append(url)  # If there's a ConnectionError exception, add the URL to the list of bad URLs
                                  # Eğer bir ConnectionError istisnası oluşursa, URL'yi kötü URL'ler listesine ekle
            continue

    # Write the good URLs to the output file
    # İyi URL'leri çıkış dosyasına yaz

    with open(out_file, 'w') as file:
        file.write('\n'.join(good_urls))

    # Print a message indicating the URLs have been saved
    # URL'lerin kaydedildiğini belirten bir iletiyi yazdır

    print(f"Saved URLS {out_file}")

# Specify the output file name
# Çıkış dosyası adını belirt

out_file = 'filtered_urls.txt'

# Call the function to filter and save URLs
# URL'leri filtrelemek ve kaydetmek için fonksiyonu çağır

urls(out_file)
