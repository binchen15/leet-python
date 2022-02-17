class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        
        from datetime import date
        
        days = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        d = date(year, month, day)
        
        return days[d.weekday()]
