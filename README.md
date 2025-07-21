# 🐱 Cat Facts API Test Suite

This is an automated test suite for the Cat Facts API(https://catfact.ninja/), built with `pytest` and `requests`.

---

| Test Name                        | Description                                                                 | Expected Result                  | Validation |
| test valid endpoints should return 200 | Check if `/fact` and `/facts?limit=3` return 200                      | Status code = 200                | `assert response.status_code == 200` |
| test fact response contains fact and length | Check if `/fact` returns fields `fact` and `length`              | Keys exist and are valid         | `assert "fact" in data` etc.   |
| test facts list has expecteds structure | Check if `/facts?limit=3` returns a list of 3 facts                  | List has 3 items                 | `assert len(data["data"]) == 3` |
| test invalid requests should fail | Test invalid paths and parameters like `/wrong`, `limit=-1`, `limit=abc`   | Status code = 400 or 404         | `assert status_code in [400,404]` |

---
