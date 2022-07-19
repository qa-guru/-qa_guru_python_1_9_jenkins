import allure
from selene import have, by


class TestRegistrationForm:

    @allure.title("Successful fill form")
    def test_successful(self, browser_chrome):
        first_name = "Alex"
        last_name = "Egorov"
        browser = browser_chrome

        @allure.step("Open registrations form")
        def open_registration_form():
            browser.open("https://demoqa.com/automation-practice-form")
            browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
            browser.driver.execute_script("$('footer').remove()")
            browser.driver.execute_script("$('#fixedban').remove()")

        open_registration_form()

        @allure.step("Fill form")
        def fill_form():
            browser.element("#firstName").set_value(first_name)
            browser.element("#lastName").set_value(last_name)
            browser.element("#userEmail").set_value("alex@egorov.com")
            browser.element("#genterWrapper").element(by.text("Other")).click()
            browser.element("#userNumber").set_value("1231231230")
            # browser.element("#dateOfBirthInput").click()
            # browser.element(".react-datepicker__month-select").s("July")
            # browser.element(".react-datepicker__year-select").selectOption("2008")
            # browser.element(".react-datepicker__day--030:not(.react-datepicker__day--outside-month)").click()
            browser.element("#subjectsInput").send_keys("Maths")
            browser.element("#subjectsInput").press_enter()
            browser.element("#hobbiesWrapper").element(by.text("Sports")).click()
            # browser.element("#uploadPicture").uploadFromClasspath("img/1.png")
            browser.element("#currentAddress").set_value("Some street 1")
            browser.element("#state").click()
            browser.element("#stateCity-wrapper").element(by.text("NCR")).click()
            browser.element("#city").click()
            browser.element("#stateCity-wrapper").element(by.text("Delhi")).click()
            browser.element("#submit").click()

        fill_form()

        @allure.step("Check form results")
        def check_form_results():
            browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
            # browser.element(".table-responsive").should(
            #     have.texts(first_name, last_name, "alex@egorov.com", "Some street 1"))

        check_form_results()
