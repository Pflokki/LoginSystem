#include "createuserwindow.h"
#include "ui_createuserwindow.h"

CreateUserWindow::CreateUserWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::CreateUserWindow)
{
    ui->setupUi(this);
}

CreateUserWindow::~CreateUserWindow()
{
    delete ui;
}
