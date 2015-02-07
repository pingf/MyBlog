from splinter import Browser
if __name__ == '__main__':
    browser = Browser('chrome')
    browser.visit('http://127.0.0.1:5000/pages/simple')
    
    if browser.is_text_present('hello world'):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... We need to improve our SEO techniques")
    
    browser.quit()