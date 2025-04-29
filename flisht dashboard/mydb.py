import mysql.connector

class mydb:
    def __init__(self):
        self.conn = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "afternoon")

        self.csr = self.conn.cursor()
    
    def get_cities(self):
        self.csr.execute("select distinct(Source) from flights_data")

        cites = []
        for i in self.csr.fetchall():
            cites.append(i[0])
        return cites

    def get_destination_ceties(self):

        self.csr.execute("SELECT distinct(Destination) FROM flights_data")

        dst_cts = []
        for i in self.csr.fetchall():
            dst_cts.append(i[0])
        
        return dst_cts
    

    def get_flights_data(self, src, dst):
        
        self.csr.execute(f"SELECT Airline, Source, Destination, Total_Stops, Price FROM afternoon.flights_data where Source = '{src}' and Destination = '{dst}'")

        flights = self.csr.fetchall()

        return flights


    def airlines_flights(self):
        self.csr.execute("SELECT Airline, count(*) as x FROM flights_data group by Airline order by x desc")

        data = self.csr.fetchall()
        airline_name = []
        flights_count = []

        for i in data:
            airline_name.append(i[0])
            flights_count.append(i[1])
        
        return airline_name, flights_count

    def buzest_airport(self):
        self.csr.execute("select source, count(*)as q from (SELECT source FROM afternoon.flights_data union all SELECT Destination FROM afternoon.flights_data) t group by t.source order by q desc")

        data = self.csr.fetchall()

        airport = []
        ct = []

        for i in data:
            airport.append(i[0])
            ct.append(i[1])
        
        return airport, ct


obj = mydb()
obj.airlines_flights()