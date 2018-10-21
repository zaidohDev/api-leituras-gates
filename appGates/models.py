from django.db import models


GATES_CHOICES = (
    ('BLQ-01', 'E-001'),
    ('BLQ-02', 'E-002'),
    ('BLQ-03', 'E-003'),
    ('BLQ-04', 'E-004'),
    ('BLQ-05', 'E-005'),
    ('BLQ-06', 'E-006'),
    ('BLQ-07', 'E-007'),
    ('BLQ-08', 'E-008'),
    ('BLQ-09', 'E-009'),
    ('BLQ-11', 'E-011'),
    ('BLQ-12', 'E-012'),
    ('BLQ-01', 'M-001'),
    ('BLQ-02', 'M-002'),
    ('BLQ-03', 'M-003'),
    ('BLQ-04', 'M-004'),
    ('BLQ-05', 'M-005'),
    ('BLQ-06', 'M-006'),
    ('BLQ-07', 'M-007'),
    ('BLQ-08', 'M-008'),
    ('BLQ-09', 'M-019'),
    ('BLQ-10', 'M-010'),
    ('BLQ-11', 'M-011'),
    ('BLQ-12', 'M-012'),
)


class Gate(models.Model):
    nome = models.CharField(max_length=255, choices=GATES_CHOICES)
    ativo = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "Gate: {0} ".format(self.nome)

    def __dir__(self):
        return object.__dict__
