import requests

headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImNiMzQ4ZWFjLTc0NzQtNGFhZi1iMGU3LWU3NjE2MTBmYzVlYiIsImlhdCI6MTY3OTg5MTI1MSwic3ViIjoiZGV2ZWxvcGVyL2IzOTkyYzMxLTkyNWQtOTZiOS02MmQ1LTJkOGQ5MWY5Mjk5YyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxMzguMTM2LjEwOC4yMDkiXSwidHlwZSI6ImNsaWVudCJ9XX0.qHyFW6Jdr7By4nBBy0Hx1CdkH0R-V2rxveb0GZQwJy3l5cQCUMFom6q9XglOErRn5g1fuWZrxN2aTceNZBkJZQ"
}

response = requests.get("https://api.clashroyale.com/v1/cards", headers=headers)

cards = response.json()
