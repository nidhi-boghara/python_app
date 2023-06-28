# will be edited as "John Doe <johndoe@gmail.com>"
def get_sender_details():
    return "Nidhi", "nidhi.b@sigzen.com"

# self - EmailQueue object refrence for updating status
def send(self, sender, recipient, msg):
    # smtp or http request
    self.update_status("Sending")
