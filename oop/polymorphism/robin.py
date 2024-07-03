from bird import Bird


class Robin(Bird):
    def sing(self):
        print("tweedle")

    def sing_again(self):
        super().sing()
