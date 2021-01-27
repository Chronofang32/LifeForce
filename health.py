class health:
    HL1 = 0
    HL2 = 0

    def healthSet(self, num, who):
        if who == "1":
            health.HL1 = num
            return health.HL1
        elif who == "2":
            health.HL2 = num
            return health.HL1
        else:
            return

    def healthSub(self, num, who):
        if who == "1":
            health.HL1 -= num
            return health.HL1
        elif who == "2":
            health.HL2 -= num
            return health.HL2
        else:
            return


