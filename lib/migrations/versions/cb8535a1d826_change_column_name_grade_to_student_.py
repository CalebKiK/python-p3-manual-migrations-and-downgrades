"""Change column name grade to student_grade

Revision ID: cb8535a1d826
Revises: 791279dd0760
Create Date: 2024-09-11 15:36:18.445556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb8535a1d826'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('grade', 'student_grade')


def downgrade() -> None:
    op.alter_column('student_grade', 'grade')
