import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

count = 0

selecFacilitys = ['Tokyo CURA Healthcare Center','Hongkong CURA Healthcare Center','Seoul CURA Healthcare Center']
selectRadio_programs = ['radio_program_medicare','radio_program_medicaid','radio_program_none']

print("--- Iniciando las pruebas con Python-Selenium ---")

try:
    # Ciclo para recorrer diferentes instalaciones y programas
    for selecFacility in selecFacilitys:
        for selectRadio_program in selectRadio_programs:
            with open('fechaComentarios.txt') as file:
                for i, line in enumerate(file):
                    fecha = (line)
                    dividir = fecha.split(";")
                    try:
                        gotdata = dividir[1]
                        fechaData = dividir[0]
                        comentarioData = dividir[1]
                    except IndexError:
                        gotdata = 'null'

                    # Inicializar el controlador de Chrome
                    driver = webdriver.Chrome()
                    driver.get("https://katalon-demo-cura.herokuapp.com/")

                    # Interacción con la página web
                    BotonMake = driver.find_element(By.ID, "btn-make-appointment")
                    BotonMake.send_keys(Keys.ENTER)

                    loginUser = driver.find_element(By.ID, "txt-username")
                    loginUser.send_keys("John Doe")

                    loginPass = driver.find_element(By.ID, "txt-password")
                    loginPass.send_keys("ThisIsNotAPassword")

                    loginBoton = driver.find_element(By.ID, "btn-login")
                    loginBoton.send_keys(Keys.ENTER)

                    facility = driver.find_element(By.ID, "combo_facility")
                    selectFacility = Select(facility)
                    selectFacility.select_by_value(selecFacility)

                    checkbox = driver.find_element(By.ID, "chk_hospotal_readmission")
                    checkbox.click()

                    radio_program = driver.find_element(By.ID, selectRadio_program)
                    radio_program.click()

                    dateVisit = driver.find_element(By.ID, "txt_visit_date")
                    dateVisit.send_keys(fechaData)

                    comentario = driver.find_element(By.ID, "txt_comment")
                    comentario.send_keys(comentarioData)

                    bookAppointment = driver.find_element(By.ID, "btn-book-appointment")
                    bookAppointment.send_keys(Keys.ENTER)

                    confirmacion = driver.find_element(By.TAG_NAME, "h2")
                    textoConfirmacion = confirmacion.text
                    count+=1

                    # Verificación de éxito o fallo de la prueba
                    if textoConfirmacion == "Appointment Confirmation":
                        print(f'La prueba #{count}, fue satisfactoria con el mensaje: {textoConfirmacion}')
                    else:
                        print(f'La prueba fallo')
                    time.sleep(1)
                    driver.quit()

except NoSuchElementException as e:
    print("Error: Elemento no encontrado -", e)

except Exception as e:
    print("Error inesperado -", e)

finally:
    # Cierre del navegador y del archivo
    driver.quit()
    file.close()
    print("--- Finalizando las pruebas con Python-Selenium ---")
