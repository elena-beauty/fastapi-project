import random

from faker.proxy import Faker
from tqdm import tqdm

from app import connection_pool
from app.constant.employee_constant import EmployeeStatus, EmployeeAllowedFields
from app.model.department import Department
from app.model.employee import Employee
from app.model.location import Location
from app.model.organization import Organization
from app.model.position import Position

fake = Faker()


def init_data(num_orgs: int = 100, num_employees: int = 1_000_000) -> None:
    with connection_pool.open_session() as session:
        organizations = []
        departments = []
        locations = []
        positions = []

        for i in tqdm(range(1, num_orgs + 1), desc='Creating initial organizations'):
            organization = Organization(
                name=fake.company(),
                domain=fake.domain_name() + str(i),
                column_config=random.sample(
                    [field for field in EmployeeAllowedFields],
                    random.randint(1, len(EmployeeAllowedFields)),
                ),
            )
            organizations.append(organization)

            for _ in range(1, 11):
                department = Department(
                    name=fake.word(),
                    description=fake.sentence(),
                    organization=organization,
                )
                departments.append(department)

                location = Location(
                    name=fake.city(),
                    address=fake.address(),
                    city=fake.city(),
                    country=fake.country(),
                    organization=organization,
                )
                locations.append(location)

                position = Position(
                    title=fake.job(),
                    level=fake.word(),
                    description=fake.sentence(),
                    organization=organization,
                )
                positions.append(position)

        session.add_all(organizations + departments + locations + positions)
        session.flush()
        for organization in organizations:
            session.refresh(organization)

        department_ids = [department.id for department in departments]
        location_ids = [location.id for location in locations]
        position_ids = [position.id for position in positions]

        employees = []
        BATCH_SIZE = min(5000, num_employees)
        for i in tqdm(range(1, num_employees + 1), desc='Creating initial employees'):
            organization = random.choice(organizations)
            employee = Employee(
                email=fake.email() + str(i),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone=fake.phone_number(),
                hire_date=fake.date_object(),
                status=EmployeeStatus.ACTIVE,
                organization_id=organization.id,
                department_id=random.choice(department_ids),
                location_id=random.choice(location_ids),
                position_id=random.choice(position_ids),
                manager_id=None,
            )
            employees.append(employee)
            if i % BATCH_SIZE:
                session.add_all(employees)
                session.flush()
                employees.clear()

        session.flush()


if __name__ == '__main__':
    init_data(num_employees=1_000)
