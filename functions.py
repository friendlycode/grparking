import logging


def add_key(byLot, key, lot):
    """
    @param byLot: dictionary of dictionaries. {day: {Lot: data}} where the data is the usage to plot.
    @param key: key to add to the dictionary
    """
    if entrytime.strftime('%A') not in byLot.keys():
        byLot[entrytime.strftime('%A')] = {}
    if lot not in byLot[entrytime.strftime('%A')].keys():
        byLot[entrytime.strftime('%A')][lot] = [0] * minutes_in_a_day
    return byLot


def graph(lot_data, lots):
    """
    @param lot_data: dictionary of dictionaries. {day: {Lot: data}} where the data is the usage to plot.

    A graph will be created for each day of the weeks.
    """
    minutes_in_a_day = 24 * 60
    suffix = ' AM'

    for i in range(25):
        if i >= 12:
            suffix = ' PM'
        xAxis[i] = str(i % 12) + str(suffix)
    xAxis[0] = "Midnight"
    xAxis[12] = "Noon"

    xticks = np.arange(0, minutes_in_a_day, 60)

    today = dt.datetime.now()
    times = [today + dt.timedelta(minutes=i) for i in range(minutes_in_a_day)]

    plt.xlabel('Time (hrs)')
    plt.ylabel('Number of Cars Parked')

    for day in byLot.keys():
        for key,value in byLot[day].iteritems():
            for i,v in enumerate(value):
                value[i] = v / 52
            plt.plot(value)
            if key in lots.keys():
                legend.append(unicode(lots[key][0]))
            else:
                legend.append(unicode(key))
        plt.title("Cars Parked on a " + day)
        plt.legend(legend, loc=2, borderaxespad=0.)
        plt.xticks(xticks, xAxis)

        for lot in lots.keys():
            if lots[lot][0] not in legend:
                logging.info("Lot ID: " + str(lot))
                logging.info("Lot Name: " + lots[lot][0])

        plt.show()
