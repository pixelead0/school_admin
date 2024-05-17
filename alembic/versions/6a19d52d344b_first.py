"""first

Revision ID: 6a19d52d344b
Revises: 
Create Date: 2024-05-17 20:05:39.028352

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a19d52d344b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'grade', ['id'])
    op.create_unique_constraint(None, 'invoice', ['id'])
    op.create_unique_constraint(None, 'payment', ['id'])
    op.create_unique_constraint(None, 'payment_type', ['id'])
    op.create_unique_constraint(None, 'school', ['id'])
    op.create_unique_constraint(None, 'student', ['id'])
    op.create_unique_constraint(None, 'users', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'student', type_='unique')
    op.drop_constraint(None, 'school', type_='unique')
    op.drop_constraint(None, 'payment_type', type_='unique')
    op.drop_constraint(None, 'payment', type_='unique')
    op.drop_constraint(None, 'invoice', type_='unique')
    op.drop_constraint(None, 'grade', type_='unique')
    # ### end Alembic commands ###
