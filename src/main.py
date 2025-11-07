"""
Activity 10: CIS Major Progress Tracker
Create a CISMajor class and track multiple student instances!
"""


class CISMajor:
    """A CIS student at Allegheny College pursuing a computing major."""
    
    def __init__(self, name, major):
        """
        Initialize a new CIS student.
        
        Args:
            name (str): The student's name
            major (str): One of: "Computer Science", "Software Engineering", 
                        "Data Science", "Informatics"
        """
        # TODO: Initialize instance attributes
        # self.name = 
        # self.major = 
        # self.credits = 0
        pass
    
    def complete_course(self, course_name, credits):
        """
        Complete a course and earn credits.
        
        Args:
            course_name (str): Name of the course (e.g., "CMPSC 100")
            credits (int): Number of credits for the course
            
        Returns:
            int: New total credits after completing course
        """
        # TODO: Add credits to self.credits
        # TODO: Print confirmation message like:
        #       "✅ Maria Garcia completed CMPSC 100 (+4 credits, total: 4)"
        # TODO: Return new total credits
        pass
    
    def get_status(self):
        """
        Get current academic status of the student.
        
        Returns:
            str: Formatted status string with name, major, and credits
        """
        # TODO: Return formatted string like:
        # "🎓 Maria Garcia | Major: Computer Science | Credits: 8"
        pass
    
    def credits_to_graduation(self):
        """
        Calculate credits remaining until graduation (48 total required).
        
        Returns:
            int: Credits needed to reach 48
        """
        # TODO: Calculate and return 48 - self.credits
        pass


# ============================================
# TEST YOUR CISMAJOR CLASS HERE
# ============================================

if __name__ == "__main__":
    print("� === CIS MAJOR PROGRESS TRACKER === �\n")
    
    # TODO: Create at least 3 student instances with different majors
    # maria = CISMajor("Maria Garcia", "Computer Science")
    # jamal = CISMajor("Jamal Washington", "Software Engineering")
    # priya = CISMajor("Priya Patel", "Data Science")
    
    # TODO: Display initial status
    # print(maria.get_status())
    # print(jamal.get_status())
    
    # TODO: Complete some courses
    # maria.complete_course("CMPSC 100", 4)
    # maria.complete_course("CMPSC 101", 4)
    # jamal.complete_course("CMPSC 100", 4)
    
    # TODO: Check graduation progress
    # print(f"{maria.name} needs {maria.credits_to_graduation()} more credits")
    # print(f"{jamal.name} needs {jamal.credits_to_graduation()} more credits")
    
    print("\n🎓 CIS Major Progress Tracker complete! 🎓")
