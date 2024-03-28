Обновление с использованием JOIN

UPDATE full_names

SET status = short_names.status

FROM short_names

WHERE full_names.name LIKE short_names.name || '.%';

Использование подзапроса

UPDATE full_names
SET status = (
    SELECT short_names.status
    FROM short_names
    WHERE full_names.name LIKE short_names.name || '.%'
    LIMIT 1
);
