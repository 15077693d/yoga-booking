location = {
    "PURE South - The Pulse": 14,
    "PURECAST Yoga Live-stream": 77,
    "Yoga - Asia Standard Tower":13,
    "Yoga - Grand Century Place": 39,
    "Yoga - Langham Place": 7,
    "Yoga - Lincoln House": 11,
    "Yoga - Millennium City 5": 40,
    "Yoga - Pacific Place": 18,
    "Yoga - Peninsula Office Tower": 5,
    "Yoga - Soundwill Plaza": 3,
    "Yoga - Starstreet Precinct": 41,
    "Yoga - The Centrium": 1,
    "Yoga - World Trade Centre": 32
}

wait_seconds = 20

xpath = {
  "sign_in_button": '//button[@id="sign-in-btn"]',
  "username_input": '//input[@id="username"]',
  "password_input": '//input[@id="password"]',
  # column etc.7:00
  "time_tr":'//tbody[@id="schedule-list"]/tr',
  # row etc.Tue Oct 6
  "date_tr": '//tr[@id="schedule-date"]/th[position() > 1]',
}