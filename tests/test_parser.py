from src.main import parse_holidays

class TestParseHolidays:
    def test_parse_holidays(self):
        html = '''
        <table align="center" border="1" cellpadding="1" cellspacing="1" summary="A table listing the public holiday dates for 2020, 2021 and 2022.">
        <caption>
          <p>
          <strong>
            Public holidays in Western Australia - 2024 to 2026
          </strong>
          </p>
        </caption>
        <thead>
          <tr>
          <th scope="row">
          </th>
          <th scope="col">
            2024
          </th>
          <th scope="col">
            2025
          </th>
          <th scope="col">
            2026
          </th>
          </tr>
        </thead>
        <tbody>
          <tr>
          <th scope="row">
            <strong>
            New Year's Day
            </strong>
          </th>
          <td>
            Monday 1 January
          </td>
          <td>
            Wednesday 1 January
          </td>
          <td>
            Thursday 1 January
          </td>
          </tr>
          <tr>
          <th scope="row">
            <strong>
            Australia Day
            </strong>
          </th>
          <td>
            Friday 26 January
          </td>
          <td>
            Monday 27 January
          </td>
          <td>
            Monday 26 January
          </td>
          </tr>
          <tr>
          <th scope="row">
            <strong>
            Labour Day
            </strong>
          </th>
          <td>
            Monday 4 March
          </td>
          <td>
            Monday 3 March
          </td>
          <td>
            Monday 2 March
          </td>
          </tr>
          <tr>
          <th scope="row">
            <strong>
            Good Friday
            </strong>
          </th>
          <td>
            Friday 29 March
          </td>
          <td>
            Friday 18 April
          </td>
          <td>
            Friday 3 April
          </td>
          </tr>
          <tr>
          <th scope="row">
            <strong>
            Easter Sunday
            </strong>
          </th>
          <td>
            Sunday 31 March *
          </td>
          <td>
            Sunday 20 April *
          </td>
          <td>
            Sunday 5 April *
          </td>
          </tr>
          <tr>
          <th scope="row">
            <strong>
            Easter Monday
            </strong>
          </th>
          <td>
            Monday 1 April
          </td>
          <td>
            Monday 21 April
          </td>
          <td>
            Monday 6 April
          </td>
          </tr>
          <tr>
          <th scope="row">
            <strong>
            Anzac Day
            </strong>
          </th>
          <td>
            Thursday 25 April
          </td>
          <td>
            Friday 25 April
          </td>
          <td>
            Saturday 25 April
            <br/>
            &amp;
            <br/>
            Monday 27 April
          </td>
          </tr>
          <tr>
          <th scope="row">
            <strong>
            Western Australia Day
            </strong>
          </th>
          <td>
            Monday 3 June
          </td>
          <td>
            Monday 2 June
          </td>
          <td>
            Monday 1 June
          </td>
          </tr>
          <tr>
          <th scope="row">
            <strong>
            King's Birthday #
            </strong>
          </th>
          <td>
            Monday 23 September
          </td>
          <td>
            Monday 29 September
          </td>
          <td>
            Monday 28 September
          </td>
          </tr>
          <tr>
          <th scope="row">
            <strong>
            Christmas Day
            </strong>
          </th>
          <td>
            Wednesday 25 December
          </td>
          <td>
            Thursday 25 December
          </td>
          <td>
            Friday 25 December
          </td>
          </tr>
          <tr>
          <th scope="row">
            <strong>
            Boxing Day
            </strong>
          </th>
          <td>
            Thursday 26 December
          </td>
          <td>
            Friday 26 December
          </td>
          <td>
            Saturday 26 December
            <br/>
            &amp;
            <br/>
            Monday 28 December
          </td>
          </tr>
        </tbody>
        </table>
        '''
        
        holidays = parse_holidays(html)
        
        expected = [
            {"Year": "2024", "Holiday Date": "Monday 1 January", "Holiday Name": "New Year's Day"},
            {"Year": "2025", "Holiday Date": "Wednesday 1 January", "Holiday Name": "New Year's Day"},
            {"Year": "2024", "Holiday Date": "Friday 26 January", "Holiday Name": "Australia Day"},
            {"Year": "2025", "Holiday Date": "Monday 27 January", "Holiday Name": "Australia Day"},
            {"Year": "2024", "Holiday Date": "Monday 4 March", "Holiday Name": "Labour Day"},
            {"Year": "2025", "Holiday Date": "Monday 3 March", "Holiday Name": "Labour Day"},
            {"Year": "2024", "Holiday Date": "Friday 29 March", "Holiday Name": "Good Friday"},
            {"Year": "2025", "Holiday Date": "Friday 18 April", "Holiday Name": "Good Friday"},
            {"Year": "2024", "Holiday Date": "Sunday 31 March (special date)", "Holiday Name": "Easter Sunday"},
            {"Year": "2025", "Holiday Date": "Sunday 20 April (special date)", "Holiday Name": "Easter Sunday"},
            {"Year": "2024", "Holiday Date": "Monday 1 April", "Holiday Name": "Easter Monday"},
            {"Year": "2025", "Holiday Date": "Monday 21 April", "Holiday Name": "Easter Monday"},
            {"Year": "2024", "Holiday Date": "Thursday 25 April", "Holiday Name": "Anzac Day"},
            {"Year": "2025", "Holiday Date": "Friday 25 April", "Holiday Name": "Anzac Day"},
            {"Year": "2024", "Holiday Date": "Monday 3 June", "Holiday Name": "Western Australia Day"},
            {"Year": "2025", "Holiday Date": "Monday 2 June", "Holiday Name": "Western Australia Day"},
            {"Year": "2024", "Holiday Date": "Monday 23 September", "Holiday Name": "King's Birthday (special holiday)"},
            {"Year": "2025", "Holiday Date": "Monday 29 September", "Holiday Name": "King's Birthday (special holiday)"},
            {"Year": "2024", "Holiday Date": "Wednesday 25 December", "Holiday Name": "Christmas Day"},
            {"Year": "2025", "Holiday Date": "Thursday 25 December", "Holiday Name": "Christmas Day"},
            {"Year": "2024", "Holiday Date": "Thursday 26 December", "Holiday Name": "Boxing Day"},
            {"Year": "2025", "Holiday Date": "Friday 26 December", "Holiday Name": "Boxing Day"}
        ]
        
        assert holidays == expected
