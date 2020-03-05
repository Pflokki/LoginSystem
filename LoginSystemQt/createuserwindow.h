#ifndef CREATEUSERWINDOW_H
#define CREATEUSERWINDOW_H

#include <QWidget>

namespace Ui {
class CreateUserWindow;
}

class CreateUserWindow : public QWidget
{
    Q_OBJECT

public:
    explicit CreateUserWindow(QWidget *parent = nullptr);
    ~CreateUserWindow();

private:
    Ui::CreateUserWindow *ui;
};

#endif // CREATEUSERWINDOW_H
