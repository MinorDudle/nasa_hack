import requests


def post_image(data, data2):
    url = 'http://localhost:5000/upload-image'
    r = requests.post(url, files=data, json=data2)
    print(r.text)


if __name__ == "__main__":

    path_to_image = ""
    post_image({'media': open(path_to_image, "rb")},
               {"T_star": 5400, "R": 2, "a": 2.5, "M_exo":1, "R_exo":1})
