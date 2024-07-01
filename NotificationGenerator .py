from plyer import notification



def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Bildirim Uygulaması',
        timeout=10
    )


if __name__ == "__main__":
    show_notification("Info", "Hello World!.")