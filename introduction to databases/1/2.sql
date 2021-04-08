select *
from billing
where payer_email='vasya@mail.com';

insert into billing values(
    'pasha@mail.com',
    'katya@mail.com',
    '300.00',
    'EUR',
    '2016-02-14',
    'Valentines day present)');

update billing  
set payer_email='igor@mail.com' 
where payer_email='alex@mail.com';

DELETE FROM billing 
    WHERE payer_email IS NULL 
    OR recipient_email IS NULL
    OR payer_email = '' 
    OR recipient_email = '';