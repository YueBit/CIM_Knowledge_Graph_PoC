from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable

class Knowledge_gragh:

    def __init__(self):
        print("KG is initiated")
        
    def connect(self, uri, user, password):
        try:
            self.driver = GraphDatabase.driver(uri, auth=(user, password))
            print("KG Connected")
            return 1
        except:
            print("KG is not connected")
            return 0

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def find_cause(self, problem_name):
        with self.driver.session(database="neo4j") as session:
            result_cause = session.read_transaction(self._find_cause_by_problem, problem_name)
            print("==="+result_cause)
            return result_cause

    @staticmethod
    def _find_cause_by_problem(tx, problem_name):
        query = (
            'MATCH (p:Problem)-[r]-(c:`Possible Cause`) '
            "WHERE p.Problems=$problem_name "
            "RETURN c.`Possible Reasons` AS cause"
        )
        result = tx.run(query, problem_name = problem_name)
        print("test1")
        for row in result:
            print(row["cause"])
        return row[0]
            
    def find_solution(self, cause_name):
        with self.driver.session(database="neo4j") as session:
            result1 = session.read_transaction(self._find_solution_by_cause, cause_name)
            print(result1)
            return result1
    
    @staticmethod
    def _find_solution_by_cause(tx, cause_name):
        query = (
            'MATCH (c:`Possible Cause`)-[r]-(s:Solution) '
            "WHERE c.`Possible Reasons`=$cause_name "
            "RETURN s.Solution AS solution"
        )
        result = tx.run(query, cause_name = cause_name)
        for row in result:
            print(row["solution"])
        return row[0]

if __name__ == "__main__":
    # Aura queries use an encrypted connection using the "neo4j+s" URI scheme
    uri = "neo4j+s://6b5c5675.databases.neo4j.io"
    user = "neo4j"
    password = "4KxVG3iBCo8GPKfK91t1sAWZLJTIo8qjt75DbpZ7tRY"
    kg = Knowledge_gragh()
    kg.connect(uri, user, password)
    problem = "Iflex used is not correctly configured in the VCATS PC"
    kg.find_cause(problem)
    cause = "In Air suspension calibration process, the iflex standard is mapped one-to-one to the VCATS PC. Each VCATS PC can communicate only to a fixed iflex standard."
    kg.find_solution(cause)
    kg.close()